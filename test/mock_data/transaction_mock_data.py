import uuid
from datetime import datetime, timezone, timedelta

from app.inners.models.entities.transaction import Transaction
from test.mock_data.account_mock_data import account_mock_data

transaction_mock_data = [
    Transaction(
        id=uuid.uuid4(),
        account_id=account_mock_data[0].id,
        sell_price=0.0,
        timestamp=datetime.now(tz=timezone.utc),
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc)
    ),
    Transaction(
        id=uuid.uuid4(),
        account_id=account_mock_data[0].id,
        sell_price=1.0,
        timestamp=datetime.now(tz=timezone.utc) + timedelta(days=1),
        created_at=datetime.now(tz=timezone.utc) + timedelta(days=1),
        updated_at=datetime.now(tz=timezone.utc) + timedelta(days=1)
    ),
    Transaction(
        id=uuid.uuid4(),
        account_id=account_mock_data[0].id,
        sell_price=2.0,
        timestamp=datetime.now(tz=timezone.utc) + timedelta(days=2),
        created_at=datetime.now(tz=timezone.utc) + timedelta(days=2),
        updated_at=datetime.now(tz=timezone.utc) + timedelta(days=2)
    ),

    Transaction(
        id=uuid.uuid4(),
        account_id=account_mock_data[1].id,
        sell_price=0.0,
        timestamp=datetime.now(tz=timezone.utc),
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc),
    ),
]
