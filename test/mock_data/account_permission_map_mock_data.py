import uuid
from datetime import datetime

from app.inners.models.entities.account_permission_map import AccountPermissionMap
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.permission_mock_data import permission_mock_data

account_permission_map_mock_data = [
    AccountPermissionMap(
        id=uuid.uuid4(),
        account_id=account_mock_data[0].id,
        permission_id=permission_mock_data[0].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    AccountPermissionMap(
        id=uuid.uuid4(),
        account_id=account_mock_data[1].id,
        permission_id=permission_mock_data[1].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
