import pandas as pd
from merlion.evaluate.forecast import ForecastMetric
from merlion.models.automl.autoprophet import AutoProphet, AutoProphetConfig
from merlion.utils import TimeSeries

from app.inner.models.value_objects.metric_forecast import MetricForecast
from app.inner.models.value_objects.prediction_forecast import PredictionForecast
from app.outer.interfaces.deliveries.contracts.requests.forecast.item_stock.stock_forecast_by_item_id_request import \
    StockForecastByItemIdRequest
from app.outer.interfaces.deliveries.contracts.responses.Content import Content
from app.outer.interfaces.deliveries.contracts.responses.forecast.item_stock_forecast_response import \
    ItemStockForecastResponse
from app.outer.repositories import inventory_control_repository


async def forecast(request: StockForecastByItemIdRequest) -> Content[ItemStockForecastResponse]:
    inventory_controls = await inventory_control_repository.read_all_by_item_id(request.item_id)

    inventory_controls_df = pd.DataFrame([value.__dict__ for value in inventory_controls])

    grouped_inventory_controls_df = inventory_controls_df \
        .sort_values(by=["timestamp"], ascending=True) \
        .groupby(by=pd.Grouper(key="timestamp", freq='1D')) \
        .first() \
        .resample(request.resample) \
        .sum()

    endogenous_data = grouped_inventory_controls_df[["quantity_before", "quantity_after"]]

    train_test_ratio = 0.8
    train_data = endogenous_data.iloc[:int(len(endogenous_data) * train_test_ratio)]
    test_data = endogenous_data.iloc[int(len(endogenous_data) * train_test_ratio):]

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
        message="Item stock forecast succeed.",
        data=ItemStockForecastResponse(
            prediction=prediction_forecast,
            metric=metric_forecast
        )
    )

    return content
