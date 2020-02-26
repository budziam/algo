# https://algorithms.tutorialhorizon.com/colorful-numbers/


def is_colorful(number: int) -> bool:
    text = str(number)

    existing = set()

    for i in range(len(text)):
        my_sum = 1
        for char in text[i:]:
            my_sum *= int(char)

            if my_sum in existing:
                return False

            existing.add(my_sum)

    return True


print(is_colorful(324))
