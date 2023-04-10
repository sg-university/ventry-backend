import uuid
from datetime import datetime

from app.inners.models.entities.company import Company

company_mock_data = [
    Company(
        id=uuid.uuid4(),
        name="name0",
        description="description0",
        address="address0",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Company(
        id=uuid.uuid4(),
        name="name1",
        description="description1",
        address="address1",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
