import uuid
from datetime import datetime

from app.inners.models.entities.item import Item
from test.mock_data.permission_mock_data import permission_mock_data

item_mock_data = [
    Item(
        id=uuid.uuid4(),
        permission_id=permission_mock_data[0].id,
        code="code0",
        name="name0",
        description="description0",
        combination_max_quantity=0.0,
        combination_min_quantity=0.0,
        quantity=0.0,
        unit_name="unit_name0",
        unit_sell_price=0.0,
        unit_cost_price=0.0,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Item(
        id=uuid.uuid4(),
        permission_id=permission_mock_data[1].id,
        code="code1",
        name="name1",
        description="description1",
        combination_max_quantity=1.0,
        combination_min_quantity=1.0,
        quantity=1.0,
        unit_name="unit_name1",
        unit_sell_price=1.0,
        unit_cost_price=1.0,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
