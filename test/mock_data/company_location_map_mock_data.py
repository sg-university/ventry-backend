import uuid
from datetime import datetime

from app.inners.models.entities.company_location_map import CompanyLocationMap
from test.mock_data.company_mock_data import company_mock_data
from test.mock_data.location_mock_data import location_mock_data

company_location_map_mock_data = [
    CompanyLocationMap(
        id=uuid.uuid4(),
        company_id=company_mock_data[0].id,
        location_id=location_mock_data[0].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    CompanyLocationMap(
        id=uuid.uuid4(),
        company_id=company_mock_data[0].id,
        location_id=location_mock_data[0].id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]
