seq = list(input('Введите последовательность чисел без пробелов\n'))
unique = set(seq)
if len(seq) == len(unique):
    print("Дубликатов нет")
else:
    print("Есть дубликаты")
