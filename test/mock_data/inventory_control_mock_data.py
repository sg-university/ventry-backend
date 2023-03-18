import uuid
from datetime import datetime, timedelta

from app.inners.models.entities.inventory_control import InventoryControl
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_mock_data import item_mock_data

inventory_control_mock_data = [
    InventoryControl(
        id=uuid.uuid4(),
        account_id=account_mock_data[0].id,
        item_id=item_mock_data[0].id,
        quantity_before=0.0,
        quantity_after=1.0,
        timestamp=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    InventoryControl(
        id=uuid.uuid4(),
        account_id=account_mock_data[1].id,
        item_id=item_mock_data[0].id,
        quantity_before=1.0,
        quantity_after=2.0,
        timestamp=datetime.now() + timedelta(days=1),
        created_at=datetime.now() + timedelta(days=1),
        updated_at=datetime.now() + timedelta(days=1),
    ),
    InventoryControl(
        id=uuid.uuid4(),
        account_id=account_mock_data[1].id,
        item_id=item_mock_data[0].id,
        quantity_before=2.0,
        quantity_after=3.0,
        timestamp=datetime.now() + timedelta(days=2),
        created_at=datetime.now() + timedelta(days=2),
        updated_at=datetime.now() + timedelta(days=2),
    ),
    InventoryControl(
        id=uuid.uuid4(),
        account_id=account_mock_data[1].id,
        item_id=item_mock_data[1].id,
        quantity_before=0.0,
        quantity_after=1.0,
        timestamp=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
