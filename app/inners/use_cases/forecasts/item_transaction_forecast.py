from datetime import timezone

import holidays
import pandas as pd
from merlion.evaluate.forecast import ForecastMetric
from merlion.models.automl.autoprophet import AutoProphet, AutoProphetConfig
from merlion.utils import TimeSeries

from app.inners.models.value_objects.contracts.requests.forecasts.item_transactions.transaction_forecast_by_item_id_request import \
    TransactionForecastByItemIdRequest
from app.inners.models.value_objects.contracts.responses.content import Content
from app.inners.models.value_objects.contracts.responses.forecast.item_transaction_forecast_response import \
    ItemTransactionForecastResponse
from app.inners.models.value_objects.forecasts.metric_forecast import MetricForecast
from app.inners.models.value_objects.forecasts.prediction_forecast import PredictionForecast
from app.inners.models.value_objects.forecasts.transaction_item_map_forecast import TransactionItemMapForecast
from app.outers.repositories.transaction_item_map_repository import TransactionItemMapRepository


class ItemTransactionForecast:
    def __init__(self):
        self.transaction_item_map_repository: TransactionItemMapRepository = TransactionItemMapRepository()

    async def forecast(self, request: TransactionForecastByItemIdRequest) -> Content[ItemTransactionForecastResponse]:
        item_transactions: [
            TransactionItemMapForecast] = await self.transaction_item_map_repository.read_all_by_item_id(
            request.item_id)

        item_transactions_df = pd.DataFrame([value.dict() for value in item_transactions])

        selected_feature_item_transactions_df = item_transactions_df[
            ["timestamp", "quantity"]
        ]

        resampled_item_transactions_df = selected_feature_item_transactions_df \
            .set_index("timestamp") \
            .resample(request.resample) \
            .sum()

        resampled_item_transactions_df.index = resampled_item_transactions_df.index.tz_convert(None)

        proportion_length = int(len(resampled_item_transactions_df) * (1 - request.test_size))
        train_data = resampled_item_transactions_df.iloc[:proportion_length]
        test_data = resampled_item_transactions_df.iloc[proportion_length:]

        if len(train_data) < 2:
            return Content(
                message="Item transaction forecast failed: Need at least 2 data to train.",
                data=None
            )

        train_data_merlion = TimeSeries.from_pd(train_data)
        test_data_merlion = TimeSeries.from_pd(test_data)
        holidays_data = [
            {
                "holiday": holiday,
                "ds": ds
            }
            for ds, holiday
            in holidays.country_holidays("ID", years=resampled_item_transactions_df.index.year.unique()).items()
        ]

        model = AutoProphet(AutoProphetConfig(target_seq_index=1, holidays=holidays_data))
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

        content: Content[ItemTransactionForecastResponse] = Content(
            message="Item transaction forecasts succeed.",
            data=ItemTransactionForecastResponse(
                prediction=prediction_forecast,
                metric=metric_forecast
            )
        )

        return content
