a = int(input('Введите номер месяца\n'))


def season(number):
    if number in [1, 2, 12]:
        return 'зима'
    elif number in [3, 4, 5]:
        return 'весна'
    elif number in [6, 7, 8]:
        return 'лето'
    else:
        return 'осень'


print(season(a))
