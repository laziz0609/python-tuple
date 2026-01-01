def juft(sonlar: tuple) -> tuple:
    return tuple(son for son in sonlar if son % 2 == 0)

numbers = (3, 6, 7, 8, 10, 11)
print(juft(numbers))