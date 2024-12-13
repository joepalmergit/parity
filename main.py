def parity(number: int) -> str:
    result = 'Odd'

    if not number % 2:
        result = 'Even'

    return result
