class Cat:
    def __init__(self, name, breed, age):
        self.__name = name
        self.__age = age
        self.__breed = breed

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_breed(self):
        return self.__breed

    def change_name(self, new_name):
        self.__name = new_name

    def change_breed(self, new_breed):
        self.__breed = new_breed

    def change_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            return "Возраст не может быть отрицательным!"


a = Cat('Mura', "Scottish", 3)
print(a.change_age(-2))
print(a.get_breed())
