import uuid
from datetime import datetime

from app.inners.models.entities.company_account_map import CompanyAccountMap
from test.mock_data.account_mock_data import account_mock_data
from test.mock_data.company_mock_data import company_mock_data

company_account_map_mock_data = [
    CompanyAccountMap(
        id=uuid.uuid4(),
        company_id=company_mock_data[0].id,
        account_id=account_mock_data[0].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    CompanyAccountMap(
        id=uuid.uuid4(),
        company_id=company_mock_data[0].id,
        account_id=account_mock_data[0].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
