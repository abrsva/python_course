class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self._age = age
        self.__breed = breed

    def get_age(self):
        return self._age


a = Cat('Mura', "Scottish", 3)
print(a.name)
print(a.get_age())
print(a.__breed)
