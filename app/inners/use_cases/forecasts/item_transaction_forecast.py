import pandas as pd
from merlion.evaluate.forecast import ForecastMetric
from merlion.models.automl.autoprophet import AutoProphet, AutoProphetConfig
from merlion.utils import TimeSeries

from app.inners.models.value_objects.metric_forecast import MetricForecast
from app.inners.models.value_objects.prediction_forecast import PredictionForecast
from app.inners.models.value_objects.transaction_item_map_forecast import TransactionItemMapForecast
from app.outers.interfaces.deliveries.contracts.requests.forecasts.item_transactions.transaction_forecast_by_item_id_request import \
    TransactionForecastByItemIdRequest
from app.outers.interfaces.deliveries.contracts.responses.content import Content
from app.outers.interfaces.deliveries.contracts.responses.forecast.item_transaction_forecast_response import \
    ItemTransactionForecastResponse
from app.outers.repositories.transaction_item_map_repository import TransactionItemMapRepository


class ItemTransactionForecast:
    def __init__(self):
        self.transaction_item_map_repository: TransactionItemMapRepository = TransactionItemMapRepository()

    async def forecast(self, request: TransactionForecastByItemIdRequest) -> Content[ItemTransactionForecastResponse]:
        item_transactions: [
            TransactionItemMapForecast] = await self.transaction_item_map_repository.read_all_by_item_id(
            request.item_id)

        item_transactions_df = pd.DataFrame([value.dict() for value in item_transactions])

        grouped_inventory_controls_df = item_transactions_df \
            .sort_values(by=["timestamp"], ascending=True) \
            .groupby(by=pd.Grouper(key="timestamp", freq='1D')) \
            .first()

        resampled_item_transactions_df = grouped_inventory_controls_df \
            .resample(request.resample) \
            .sum()

        endogenous_data = resampled_item_transactions_df[["quantity"]]

        train_data = endogenous_data.iloc[:int(len(endogenous_data) - request.test_size)]
        test_data = endogenous_data.iloc[int(len(endogenous_data) - request.test_size):]

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
            message="Item transaction forecasts succeed.",
            data=ItemTransactionForecastResponse(
                prediction=prediction_forecast,
                metric=metric_forecast
            )
        )

        return content
