import time

birthday = input("Введите дату рождения (дд.мм.гггг):")
days = round((time.time() - time.mktime(time.strptime(birthday, '%d.%m.%Y'))) / 86400)
print(days)
