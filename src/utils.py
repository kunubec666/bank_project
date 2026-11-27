import json
import os
from typing import Any


def get_transactions_from_json(file_path: str) -> list[dict[str, Any]]:
    """Принимает путь к JSON-файлу и возвращает список словарей с транзакциями."""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []
