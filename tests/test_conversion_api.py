from http import HTTPStatus
from fastapi.testclient import TestClient
from app.main import app
from fixtures import *

client = TestClient(app)


def test_convert_currency_success(mock_conversion_service):
    from_currency = "USD"
    to_currency = "EUR"
    amount = 100
    mock_converted_amount = 85

    mock_conversion_service.convert.return_value = mock_converted_amount

    response = client.get(
        f"/api/convert?from={from_currency}&to={to_currency}&amount={amount}"
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["from_currency"] == from_currency
    assert data["to_currency"] == to_currency
    assert data["original_amount"] == amount
    assert data["converted_amount"] == mock_converted_amount


def test_convert_currency_invalid_currency(mock_conversion_service):
    from_currency = "XYZ"
    to_currency = "USD"
    amount = 100

    response = client.get(
        f"/api/convert?from={from_currency}&to={to_currency}&amount={amount}"
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert "detail" in response.json()


def test_convert_currency_missing_parameter(mock_conversion_service):
    from_currency = "USD"
    to_currency = "EUR"

    response = client.get(f"/api/convert?from={from_currency}&to={to_currency}")

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
