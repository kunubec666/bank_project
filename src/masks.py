def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формат XXXX XX** **** XXXX."""
    cleaned_number = card_number.replace(" ", "")

    if len(cleaned_number) != 16:
        return "Неверный формат номера карты"

    part1 = cleaned_number[:4]
    part2 = cleaned_number[4:6]
    part4 = cleaned_number[12:]

    return f"{part1} {part2}** **** {part4}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формат **XXXX."""
    if len(account_number) < 4:
        return "Неверный формат номера счета"

    last_four = account_number[-4:]
    return f"**{last_four}"
