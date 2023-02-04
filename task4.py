c = int(input("Введите число\n"))
temp = c
backward = 0
while c > 0:
    a = c % 10
    backward = backward*10 + a
    c = c // 10
if temp == backward:
    print('Это палиндром')
else:
    print('Это не палиндром')
