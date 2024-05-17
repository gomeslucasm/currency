import pytest
from unittest.mock import Mock
from unittest.mock import patch
from app.services.conversion import ConversionService
from app.repositories.currency import ExchangeRateAPIRepository


@pytest.fixture
def mock_exchange_rate_repository():
    mock_repository = Mock(spec=ExchangeRateAPIRepository)
    return mock_repository


@pytest.fixture
def conversion_service(mock_exchange_rate_repository):
    return ConversionService(exchange_rate_repository=mock_exchange_rate_repository)


@pytest.fixture
def mock_conversion_service():
    with patch("app.apis.conversion.get_conversion_service") as mock:
        mock_service = mock.return_value
        yield mock_service
