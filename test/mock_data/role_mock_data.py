import uuid
from datetime import datetime, timezone

from app.inners.models.entities.role import Role

role_mock_data = [
    Role(
        id=uuid.uuid4(),
        name="name0",
        description="description0",
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc)
    ),
    Role(
        id=uuid.uuid4(),
        name="name1",
        description="description1",
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc)
    ),
]
