import uuid
from datetime import datetime

from app.inners.models.entities.item_file_map import ItemFileMap
from test.mock_data.file_mock_data import file_mock_data
from test.mock_data.item_mock_data import item_mock_data

item_file_map_mock_data = [
    ItemFileMap(
        id=uuid.uuid4(),
        item_id=item_mock_data[0].id,
        file_id=file_mock_data[0].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    ItemFileMap(
        id=uuid.uuid4(),
        item_id=item_mock_data[0].id,
        file_id=file_mock_data[0].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
