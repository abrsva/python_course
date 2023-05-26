class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed

    def __get_age(self):
        return self.age

    def is_a_kitten(self):
        a = self.__get_age()
        if a > 1:
            print("This is an adult cat")
        else:
            print("This is a little kitten ^_^")


a = Cat('Mura', "Scottish", 0.6)
print(a.is_a_kitten())
