import uuid
from datetime import datetime

from app.inner.models.entities.inventory_control import InventoryControl
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.item_mock_data import item_mock_data

inventory_control_mock_data = [
    InventoryControl(
        id=uuid.uuid4(),
        account_id=account_mock_data[0].id,
        item_id=item_mock_data[0].id,
        quantity_before=0.0,
        quantity_after=0.0,
        timestamp=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    InventoryControl(
        id=uuid.uuid4(),
        account_id=account_mock_data[1].id,
        item_id=item_mock_data[1].id,
        quantity_before=1.0,
        quantity_after=1.0,
        timestamp=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
