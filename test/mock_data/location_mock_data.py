import uuid
from datetime import datetime

from app.inners.models.entities.location import Location

location_mock_data = [
    Location(
        id=uuid.uuid4(),
        name="name0",
        description="description0",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Location(
        id=uuid.uuid4(),
        name="name1",
        description="description1",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
