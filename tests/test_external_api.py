from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


def test_convert_to_rub_ruble() -> None:
    """Тест возврата суммы для рублевой транзакции без запроса к API."""
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rub(transaction) == 100.50


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: Mock) -> None:
    """Тест конвертации USD в RUB через мок API."""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9000.0}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"},
        }
    }
    assert convert_to_rub(transaction) == 9000.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get: Mock) -> None:
    """Тест конвертации EUR в RUB через мок API."""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 10000.0}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"},
        }
    }
    assert convert_to_rub(transaction) == 10000.0
    mock_get.assert_called_once()


def test_convert_to_rub_unknown_currency() -> None:
    """Тест поведения при неизвестной валюте."""
    transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {"code": "GBP"},
        }
    }
    assert convert_to_rub(transaction) == 50.0
