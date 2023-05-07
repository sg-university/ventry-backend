import uuid
from datetime import datetime, timezone

from app.inners.models.entities.location import Location
from test.mock_data.company_mock_data import company_mock_data

location_mock_data = [
    Location(
        id=uuid.uuid4(),
        company_id=company_mock_data[0].id,
        name="name0",
        description="description0",
        address="address0",
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc)
    ),
    Location(
        id=uuid.uuid4(),
        company_id=company_mock_data[1].id,
        name="name1",
        description="description1",
        address="address1",
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc)
    ),
]
