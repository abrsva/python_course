a = int(input('Введите номер месяца\n'))


def season(number):
    if number in [1, 2, 12]:
        print('зима')
    elif number in [3,4,5]:
        print('весна')
    elif number in [6, 7, 8]:
        print('лето')
    else: print('осень')


season(a)


