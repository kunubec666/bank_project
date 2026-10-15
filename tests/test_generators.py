import os
import sys
from typing import Any, Dict, List

# Жестко прописываем путь к корню, чтобы pytest сразу видел папку src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура, которая генерирует тестовый список транзакций."""
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод частному лицу"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата услуг"},
    ]


def test_filter_by_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию транзакций по валюте."""
    usd_gen = filter_by_currency(sample_transactions, "USD")
    result = list(usd_gen)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует поочередное извлечение описаний операций."""
    desc_gen = transaction_descriptions(sample_transactions)
    result = list(desc_gen)
    assert result == ["Перевод организации", "Перевод частному лицу", "Оплата услуг"]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (999, 1000, ["0000 0000 0000 0999", "0000 0000 0000 1000"]),
    ],
)

def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    """Параметризованный тест проверяет генерацию номеров карт в диапазонах."""
    card_gen = card_number_generator(start, stop)
    assert list(card_gen) == expected
