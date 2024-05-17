import pytest
from app.services.conversion import ConversionService
from app.repositories.currency import ExchangeRate
from fixtures import *


def test_convert_usd_to_eur(
    conversion_service: ConversionService, mock_exchange_rate_repository
):
    from_currency = "USD"
    to_currency = "EUR"
    amount = 100
    mock_rate = 0.85

    mock_exchange_rate_repository.get_exchange_rate.return_value = ExchangeRate(
        base_currency=from_currency, target_currency=to_currency, rate=mock_rate
    )

    result = conversion_service.convert(from_currency, to_currency, amount)

    assert result == amount * mock_rate
    mock_exchange_rate_repository.get_exchange_rate.assert_called_once_with(
        from_currency, to_currency
    )


def test_convert_brl_to_usd(
    conversion_service: ConversionService, mock_exchange_rate_repository
):
    from_currency = "BRL"
    to_currency = "USD"
    amount = 100
    mock_rate = 0.20

    mock_exchange_rate_repository.get_exchange_rate.return_value = ExchangeRate(
        base_currency=from_currency, target_currency=to_currency, rate=mock_rate
    )

    result = conversion_service.convert(from_currency, to_currency, amount)

    assert result == amount * mock_rate
    mock_exchange_rate_repository.get_exchange_rate.assert_called_once_with(
        from_currency, to_currency
    )


def test_convert_btc_to_eth(
    conversion_service: ConversionService, mock_exchange_rate_repository
):
    from_currency = "BTC"
    to_currency = "ETH"
    amount = 1
    mock_btc_to_usd_rate = 50000
    mock_usd_to_eth_rate = 30

    mock_exchange_rate_repository.get_exchange_rate.side_effect = [
        ExchangeRate(
            base_currency="BTC", target_currency="USD", rate=mock_btc_to_usd_rate
        ),
        ExchangeRate(
            base_currency="USD", target_currency="ETH", rate=mock_usd_to_eth_rate
        ),
    ]

    result = conversion_service.convert(from_currency, to_currency, amount)

    expected_result = amount * mock_btc_to_usd_rate * mock_usd_to_eth_rate
    assert result == expected_result
    assert mock_exchange_rate_repository.get_exchange_rate.call_count == 2
    mock_exchange_rate_repository.get_exchange_rate.assert_any_call("BTC", "USD")
    mock_exchange_rate_repository.get_exchange_rate.assert_any_call("USD", "ETH")


def test_convert_invalid_currency(
    conversion_service: ConversionService, mock_exchange_rate_repository
):
    from_currency = "XYZ"
    to_currency = "USD"
    amount = 100

    with pytest.raises(ValueError):
        conversion_service.convert(from_currency, to_currency, amount)

    mock_exchange_rate_repository.get_exchange_rate.assert_not_called()
