import uuid
from datetime import datetime

from app.inner.models.entities.file import File

file_mock_data = [
    File(
        id=uuid.uuid4(),
        name="name0",
        description="description0",
        extension="extension0",
        content="content0".encode(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    File(
        id=uuid.uuid4(),
        name="name1",
        description="description1",
        extension="extension1",
        content="content1".encode(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
