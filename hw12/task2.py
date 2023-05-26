class BankAccount:
    def __init__(self, owner, account_number, balance, password):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.__password = password

    def check_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            print('Wrong password')

    def withdraw_money(self, password, amount):
        if password != self.__password:
            print('Wrong password')
        elif amount > self.__balance:
            print('Not enough money on the account')
        else:
            self.__balance -= amount
            print(f"{amount} roubles has been successfully withdrawn from your account")

    def put_money(self, password, amount):
        if password != self.__password:
            print('Wrong password')
        else:
            self.__balance += amount
            print(f"{amount} roubles has been successfully put into your account")


a = BankAccount('Artem Kovalev', 365889, 500, '357')
print(a.owner, a.check_balance('357'))
print(a.check_balance('1997'))
a.put_money('357', 100)
a.withdraw_money('357', 150)
print(a.check_balance('357'))
