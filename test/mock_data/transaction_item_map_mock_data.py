import uuid
from datetime import datetime, timedelta

from app.inners.models.entities.transaction_item_map import TransactionItemMap
from test.mock_data.item_mock_data import item_mock_data
from test.mock_data.transaction_mock_data import transaction_mock_data

transaction_item_map_mock_data = [
    TransactionItemMap(
        id=uuid.uuid4(),
        transaction_id=transaction_mock_data[0].id,
        item_id=item_mock_data[0].id,
        sell_price=0.0,
        quantity=0.0,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    TransactionItemMap(
        id=uuid.uuid4(),
        transaction_id=transaction_mock_data[1].id,
        item_id=item_mock_data[0].id,
        sell_price=1.0,
        quantity=1.0,
        created_at=datetime.now() + timedelta(days=1),
        updated_at=datetime.now() + timedelta(days=1),
    ),
    TransactionItemMap(
        id=uuid.uuid4(),
        transaction_id=transaction_mock_data[2].id,
        item_id=item_mock_data[0].id,
        sell_price=2.0,
        quantity=2.0,
        created_at=datetime.now() + timedelta(days=2),
        updated_at=datetime.now() + timedelta(days=2),
    ),
    TransactionItemMap(
        id=uuid.uuid4(),
        transaction_id=transaction_mock_data[1].id,
        item_id=item_mock_data[1].id,
        sell_price=0.0,
        quantity=0.0,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
