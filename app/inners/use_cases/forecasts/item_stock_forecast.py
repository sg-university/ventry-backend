import pandas as pd
from merlion.evaluate.forecast import ForecastMetric
from merlion.models.automl.autoprophet import AutoProphet, AutoProphetConfig
from merlion.utils import TimeSeries

from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.models.value_objects.metric_forecast import MetricForecast
from app.inners.models.value_objects.prediction_forecast import PredictionForecast
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_stocks.stock_forecast_by_item_id_request import \
    StockForecastByItemIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.interfaces.deliveries.contracts.responses.forecast.item_stock_forecast_response import \
    ItemStockForecastResponse
from app.outers.repositories.inventory_control_repository import InventoryControlRepository


class ItemStockForecast:
    def __init__(self):
        self.inventory_control_repository: InventoryControlRepository = InventoryControlRepository()

    async def forecast(self, request: StockForecastByItemIdRequest) -> Content[ItemStockForecastResponse]:
        inventory_controls: [InventoryControl] = await self.inventory_control_repository.read_all_by_item_id(
            request.item_id)

        inventory_controls_df = pd.DataFrame([value.dict() for value in inventory_controls])

        selected_feature_inventory_controls_df = inventory_controls_df[
            ["timestamp", "quantity_before", "quantity_after"]
        ]

        resampled_inventory_controls_df = selected_feature_inventory_controls_df \
            .set_index("timestamp") \
            .resample(request.resample) \
            .sum()

        train_data = resampled_inventory_controls_df.iloc[
                     :int(len(resampled_inventory_controls_df) - request.test_size)
                     ]
        test_data = resampled_inventory_controls_df.iloc[
                    int(len(resampled_inventory_controls_df) - request.test_size):
                    ]

        train_data_merlion = TimeSeries.from_pd(train_data)
        test_data_merlion = TimeSeries.from_pd(test_data)

        model = AutoProphet(AutoProphetConfig(target_seq_index=1))
        model.train(
            train_data=train_data_merlion
        )

        prediction, prediction_error = model.forecast(
            time_stamps=len(test_data_merlion) + request.horizon,
        )

        smape_metric = ForecastMetric.sMAPE.value(
            ground_truth=test_data_merlion,
            predict=prediction,
            target_seq_index=model.target_seq_index
        )

        mae_metric = ForecastMetric.MAE.value(
            ground_truth=test_data_merlion,
            predict=prediction,
            target_seq_index=model.target_seq_index
        )

        prediction_forecast = PredictionForecast(
            past=pd.concat([train_data_merlion.to_pd(), test_data_merlion.to_pd()]).to_dict(orient='records'),
            future=prediction.to_pd().drop(test_data_merlion.to_pd().index).to_dict(orient='records')
        )

        metric_forecast = MetricForecast(
            smape=smape_metric,
            mae=mae_metric
        )

        content: Content[ItemStockForecastResponse] = Content(
            message="Item stock forecasts succeed.",
            data=ItemStockForecastResponse(
                prediction=prediction_forecast,
                metric=metric_forecast
            )
        )

        return content
