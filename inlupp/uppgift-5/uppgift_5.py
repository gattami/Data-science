# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(ls: list) -> list:
    """
    Skriv beskrivning här.
    """
    re = []
    for number in ls:
        if number % 2 == 0:
            re.append(number)
    return re
