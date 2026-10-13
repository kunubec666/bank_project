import os
import sys
from typing import Any, Dict, List

# Жестко прописываем путь к корню проекта в системные пути Python,
# чтобы утилита pytest сразу видела папку src на любом компьютере.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Фикстура генерирует стандартный список словарей для тестов."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18"},
        {"id": 2, "state": "CANCELED", "date": "2024-03-12T02:26:18"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-10T02:26:18"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", []),
    ],
)
def test_filter_by_state(sample_data: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    """Параметризованный тест проверяет фильтрацию словарей по разным статусам."""
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


def test_sort_by_date_desc(sample_data: List[Dict[str, Any]]) -> None:
    """Тест проверяет сортировку дат по убыванию (от свежих к старым)."""
    result = sort_by_date(sample_data, reverse=True)
    assert [item["id"] for item in result] == [2, 1, 3]


def test_sort_by_date_asc(sample_data: List[Dict[str, Any]]) -> None:
    """Тест проверяет сортировку дат по возрастанию (от старых к новым)."""
    result = sort_by_date(sample_data, reverse=False)
    assert [item["id"] for item in result] == [3, 1, 2]
