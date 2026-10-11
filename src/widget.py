from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счета, сохраняя текстовое название."""
    if not info_string or info_string.isspace():
        return "Некорректный ввод"

    # Разбиваем строку на слова
    parts = info_string.split()

    if len(parts) < 2:
        return "Некорректный ввод"

    # Номер всегда идет последним элементом
    number = parts[-1]
    # Все, что идет до номера — это название карты или счета
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Преобразует строку даты ISO-формата в формат ДД.ММ.ГГГГ."""
    try:
        # Парсим строку в объект datetime (обрабатывает любые корректные ISO строки)
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"


