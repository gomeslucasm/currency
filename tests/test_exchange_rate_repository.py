import pytest
import requests_mock
from app.repositories.currency import ExchangeRateAPIRepository
from app.entities.currency import ExchangeRate


def test_get_exchange_rate_success():
    base_currency = "USD"
    target_currency = "EUR"
    mock_rate = 0.85

    with requests_mock.Mocker() as m:
        m.get(
            f"https://api.exchangerate-api.com/v4/latest/{base_currency}",
            json={"rates": {target_currency: mock_rate}},
        )

        repository = ExchangeRateAPIRepository()
        exchange_rate = repository.get_exchange_rate(base_currency, target_currency)

        assert exchange_rate.base_currency == base_currency
        assert exchange_rate.target_currency == target_currency
        assert exchange_rate.rate == mock_rate


def test_get_exchange_rate_no_rate():
    base_currency = "USD"
    target_currency = "XYZ"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://api.exchangerate-api.com/v4/latest/{base_currency}",
            json={"rates": {"EUR": 0.85}},
        )

        repository = ExchangeRateAPIRepository()

        with pytest.raises(
            ValueError, match=f"No exchange rate found for {target_currency}"
        ):
            repository.get_exchange_rate(base_currency, target_currency)


def test_get_exchange_rate_http_error():
    base_currency = "USD"
    target_currency = "EUR"

    with requests_mock.Mocker() as m:
        m.get(
            f"https://api.exchangerate-api.com/v4/latest/{base_currency}",
            status_code=500,
        )

        repository = ExchangeRateAPIRepository()

        with pytest.raises(Exception, match="Error fetching exchange rates"):
            repository.get_exchange_rate(base_currency, target_currency)
