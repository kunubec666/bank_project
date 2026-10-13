import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("НекорректнаяСтрока", "Некорректный ввод"),
        ("", "Некорректный ввод"),
    ],
)
def test_mask_account_card(info: str, expected: str) -> None:
    """Проверяет универсальность распознавания карт и счетов виджетом."""
    assert mask_account_card(info) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-31T23:59:59", "31.12.2025"),
        ("invalid-date", "Неверный формат даты"),
        ("", "Неверный формат даты"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    """Проверяет перевод строк формата ISO в формат ДД.ММ.ГГГГ."""
    assert get_date(date_str) == expected
