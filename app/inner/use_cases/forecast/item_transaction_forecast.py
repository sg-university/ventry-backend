import pandas as pd
from merlion.evaluate.forecast import ForecastMetric
from merlion.models.automl.autoprophet import AutoProphet, AutoProphetConfig
from merlion.utils import TimeSeries

from app.inner.models.value_objects.transaction_item_map_forecast import TransactionItemMapForecast
from app.inner.models.value_objects.metric_forecast import MetricForecast
from app.inner.models.value_objects.prediction_forecast import PredictionForecast
from app.outer.interfaces.deliveries.contracts.requests.forecast.item_transaction.transaction_forecast_by_item_id_request import \
    TransactionForecastByItemIdRequest
from app.outer.interfaces.deliveries.contracts.responses.content import Content
from app.outer.interfaces.deliveries.contracts.responses.forecast.item_transaction_forecast_response import \
    ItemTransactionForecastResponse
from app.outer.repositories import transaction_item_map_repository


async def forecast(request: TransactionForecastByItemIdRequest) -> Content[ItemTransactionForecastResponse]:
    item_transactions: [TransactionItemMapForecast] = await transaction_item_map_repository.read_all_by_item_id(
        request.item_id)

    item_transactions_df = pd.DataFrame([value.__dict__ for value in item_transactions])

    grouped_item_transactions_df = item_transactions_df \
        .sort_values(by=["timestamp"], ascending=True) \
        .groupby(by=pd.Grouper(key="timestamp", freq='1D')) \
        .first() \
        .resample(request.resample) \
        .sum()

    endogenous_data = grouped_item_transactions_df[["quantity"]]

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

    content: Content[ItemTransactionForecastResponse] = Content(
        message="Item transaction forecast succeed.",
        data=ItemTransactionForecastResponse(
            prediction=prediction_forecast,
            metric=metric_forecast
        )
    )

    return content
