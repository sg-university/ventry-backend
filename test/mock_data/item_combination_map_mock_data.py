import uuid
from datetime import datetime

from app.inners.models.entities.item_combination_map import ItemCombinationMap
from test.mock_data.item_mock_data import item_mock_data

item_combination_map_mock_data = [
    ItemCombinationMap(
        id=uuid.uuid4(),
        super_item_id=item_mock_data[0].id,
        sub_item_id=item_mock_data[0].id,
        quantity=0.0,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    ItemCombinationMap(
        id=uuid.uuid4(),
        super_item_id=item_mock_data[1].id,
        sub_item_id=item_mock_data[1].id,
        quantity=1.0,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
