from datetime import timezone

import pandas as pd
from merlion.evaluate.forecast import ForecastMetric
from merlion.models.automl.autoprophet import AutoProphet, AutoProphetConfig
from merlion.utils import TimeSeries

from app.inners.models.entities.inventory_control import InventoryControl
from app.inners.models.value_objects.contracts.requests.forecasts.item_stocks.stock_forecast_by_item_id_request import \
    StockForecastByItemIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.models.value_objects.contracts.responses.forecast.item_stock_forecast_response import \
    ItemStockForecastResponse
from app.inners.models.value_objects.forecasts.metric_forecast import MetricForecast
from app.inners.models.value_objects.forecasts.prediction_forecast import PredictionForecast
from app.outers.repositories.inventory_control_repository import InventoryControlRepository


class ItemStockForecast:
    def __init__(self):
        self.inventory_control_repository: InventoryControlRepository = InventoryControlRepository()

    async def forecast(self, request: StockForecastByItemIdRequest) -> Content[ItemStockForecastResponse]:
        inventory_controls: [InventoryControl] = await self.inventory_control_repository.read_all_by_item_id(
            request.item_id)

        inventory_controls_df = pd.DataFrame([value.dict() for value in inventory_controls])

        selected_feature_inventory_controls_df = inventory_controls_df[
            ["timestamp", "quantity_after"]
        ]

        resampled_inventory_controls_df = selected_feature_inventory_controls_df \
            .set_index("timestamp") \
            .sort_index(ascending=True) \
            .resample(request.resample) \
            .sum()

        resampled_inventory_controls_df.index = resampled_inventory_controls_df.index.tz_convert(None)

        proportion_length = int(len(resampled_inventory_controls_df) * (1 - request.test_size))
        train_data = resampled_inventory_controls_df.iloc[:proportion_length]
        test_data = resampled_inventory_controls_df.iloc[proportion_length:]

        if len(train_data) < 2:
            return Content(
                message="Item stock forecast failed: Need at least 2 data to train.",
                data=None
            )

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

        past_df = pd.concat([train_data_merlion.to_pd(), test_data_merlion.to_pd()])
        past_df.index = past_df.index.tz_localize(timezone.utc)
        past_df = past_df.reset_index(names="timestamp")

        future_df = prediction.to_pd().drop(test_data_merlion.to_pd().index)
        future_df.index = future_df.index.tz_localize(timezone.utc)
        future_df = future_df.reset_index(names="timestamp")

        prediction_forecast = PredictionForecast(
            past=past_df.to_dict(orient='records'),
            future=future_df.to_dict(orient='records')
        )

        metric_forecast = MetricForecast(
            smape=smape_metric,
            mae=mae_metric
        )

        content: Content[ItemStockForecastResponse] = Content(
            message="Item stock forecast succeed.",
            data=ItemStockForecastResponse(
                prediction=prediction_forecast,
                metric=metric_forecast
            )
        )

        return content
