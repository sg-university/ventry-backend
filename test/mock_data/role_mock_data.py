import uuid
from datetime import datetime

from app.inner.models.entities.role import Role

role_mock_data = [
    Role(
        id=uuid.uuid4(),
        name="name0",
        description="description0",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Role(
        id=uuid.uuid4(),
        name="name1",
        description="description1",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
