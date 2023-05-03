import uuid
from datetime import datetime, timezone

from app.inners.models.entities.item_bundle_map import ItemBundleMap
from test.mock_data.item_mock_data import item_mock_data

item_bundle_map_mock_data = [
    ItemBundleMap(
        id=uuid.uuid4(),
        super_item_id=item_mock_data[0].id,
        sub_item_id=item_mock_data[0].id,
        quantity=0.0,
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc)
    ),
    ItemBundleMap(
        id=uuid.uuid4(),
        super_item_id=item_mock_data[1].id,
        sub_item_id=item_mock_data[1].id,
        quantity=1.0,
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc)
    ),
]
