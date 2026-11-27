import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Принимает транзакцию и возвращает сумму в рублях (float)."""
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0.0))
    currency_code = operation_amount.get("currency", {}).get("code")

    if currency_code == "RUB":
        return amount

    if currency_code in ("USD", "EUR"):
        api_key = os.getenv("API_KEY")
        url = "https://apilayer.com"
        params = {
            "to": "RUB",
            "from": currency_code,
            "amount": amount,
        }
        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        result = response.json().get("result", 0.0)
        return float(result)

    return amount
