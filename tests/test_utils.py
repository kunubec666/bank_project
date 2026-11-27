from unittest.mock import mock_open, patch

from src.utils import get_transactions_from_json


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]')
def test_get_transactions_success(mock_file: mock_open, mock_exists: patch) -> None:
    """Тест успешного чтения списка транзакций из JSON."""
    assert get_transactions_from_json("data/operations.json") == [{"id": 1}]


@patch("os.path.exists", return_value=False)
def test_get_transactions_file_not_found(mock_exists: patch) -> None:
    """Тест возврата пустого списка, если файл не найден."""
    assert get_transactions_from_json("missing.json") == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='{"id": 1}')
def test_get_transactions_not_list(mock_file: mock_open, mock_exists: patch) -> None:
    """Тест возврата пустого списка, если в JSON не список."""
    assert get_transactions_from_json("data/operations.json") == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_transactions_empty_file(mock_file: mock_open, mock_exists: patch) -> None:
    """Тест возврата пустого списка при пустом или битом файле."""
    assert get_transactions_from_json("data/operations.json") == []
