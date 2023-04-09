import uuid
from datetime import datetime

from app.inners.models.entities.account import Account
from test.mock_data.location_mock_data import location_mock_data
from test.mock_data.role_mock_data import role_mock_data

account_mock_data = [
    Account(
        id=uuid.uuid4(),
        role_id=role_mock_data[0].id,
        location_id=location_mock_data[0].id,
        name="name0",
        email="email0",
        password="password0",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    Account(
        id=uuid.uuid4(),
        role_id=role_mock_data[1].id,
        location_id=location_mock_data[1].id,
        name="name1",
        email="email1",
        password="password1",
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
