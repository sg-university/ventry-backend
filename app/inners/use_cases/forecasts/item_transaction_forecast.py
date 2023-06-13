from datetime import timezone

import pandas as pd
from autogluon.timeseries import TimeSeriesDataFrame, TimeSeriesPredictor

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

        if len(item_transactions) < 2:
            return Content(
                message="Item transaction forecast failed: Need at least 2 data.",
                data=None
            )

        item_transactions_df = pd.DataFrame([value.dict() for value in item_transactions])

        selected_feature_item_transactions_df = item_transactions_df[
            ["timestamp", "quantity"]
        ]

        resampled_item_transactions_df = selected_feature_item_transactions_df \
            .set_index("timestamp") \
            .resample(request.resample) \
            .sum()

        resampled_item_transactions_df.index = resampled_item_transactions_df.index.tz_convert(None)
        resampled_item_transactions_df.reset_index(names=["timestamp"], inplace=True)
        resampled_item_transactions_df["item_id"] = str(request.item_id)

        data_autogluon = TimeSeriesDataFrame.from_data_frame(
            resampled_item_transactions_df,
            id_column="item_id",
            timestamp_column="timestamp"
        )

        test_length = int(len(data_autogluon) * request.test_size)
        train_data_autogluon = data_autogluon.slice_by_timestep(None, -test_length)
        test_data_autogluon = data_autogluon

        prediction_length = test_length + request.horizon
        predictor = TimeSeriesPredictor(
            prediction_length=prediction_length,
            target="quantity",
            eval_metric=request.eval_metric,
        )

        predictor.fit(
            train_data_autogluon,
            presets="best_quality",
        )

        prediction = predictor.predict(train_data_autogluon)
        evaluation = predictor.evaluate(test_data_autogluon)

        past_df = test_data_autogluon.copy(deep=True)
        past_df.index = past_df["timestamp"].tz_localize(timezone.utc)

        future_df = prediction.slice_by_timestep(-request.horizon + 1, None)
        future_df.index = future_df["timestamp"].tz_localize(timezone.utc)

        prediction_forecast = PredictionForecast(
            past=past_df.to_dict(orient='records'),
            future=future_df.to_dict(orient='records')
        )

        metric_forecast = MetricForecast(
            name=request.eval_metric,
            result=evaluation
        )

        content: Content[ItemTransactionForecastResponse] = Content(
            message="Item transaction forecasts succeed.",
            data=ItemTransactionForecastResponse(
                prediction=prediction_forecast,
                metric=metric_forecast
            )
        )

        return content
