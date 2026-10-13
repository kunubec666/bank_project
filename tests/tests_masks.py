import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("12345", "Неверный формат номера карты"),
        ("", "Неверный формат номера карты"),
    ],
)
def test_get_mask_card_number(card_num: str, expected: str) -> None:
    """Проверяет маскирование карт разной длины и пустых строк."""
    assert get_mask_card_number(card_num) == expected


@pytest.mark.parametrize(
    "account_num, expected",
    [
        ("73654108430135874305", "**4305"),
        ("123456", "**3456"),
        ("123", "Неверный формат номера счета"),
        ("", "Неверный формат номера счета"),
    ],
)
def test_get_mask_account(account_num: str, expected: str) -> None:
    """Проверяет маскирование счетов и защиту от короткого ввода."""
    assert get_mask_account(account_num) == expected
