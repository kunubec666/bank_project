from typing import Any, Dict, Iterable, List


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency: str
) -> Iterable[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте и возвращает итератор.

    Принимает список словарей-транзакций и код валюты (например, 'USD').
    Поочередно выдает транзакции, соответствующие условию, через yield.
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})

        if currency_info.get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterable[str]:
    """Принимает список словарей с транзакциями и поочередно выдает описание операции.

    Если описание отсутствует, выдает пустую строку.
    """
    for transaction in transactions:
        # Извлекаем значение по ключу "description". 
        # Если ключа нет, метод .get() безопасно вернет пустую строку, защищая код от KeyError.
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterable[str]:
    """Генерирует номера банковских карт в заданном диапазоне от start до stop.

    Форматирует числа в строку вида XXXX XXXX XXXX XXXX с ведущими нулями.
    """
    # Цикл идет до stop включительно, поэтому прибавляем 1
    for number in range(start, stop + 1):
        # Превращаем число в 16-значную строку, заполняя пустые места нулями слева
        card_str = f"{number:016d}"
        
        # Нарезаем строку на 4 блока по 4 цифры и склеиваем их через пробел
        formatted_card = f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        
        yield formatted_card
