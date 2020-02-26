# https://algorithms.tutorialhorizon.com/colorful-numbers/
from math import log10


def is_colorful(number: int) -> bool:
    number = abs(number)
    existing = set()
    length = int(log10(number)) + 1 if number else 1

    size = 10 ** length
    while size > 1:
        current_number = number % size
        result = 1

        size_for_iteration = size
        while size_for_iteration > 1:
            current_digit = (current_number % size_for_iteration) // (size_for_iteration / 10)
            result *= current_digit

            if result in existing:
                return False

            existing.add(result)
            size_for_iteration //= 10

        size //= 10

    return True


print(is_colorful(3245))
