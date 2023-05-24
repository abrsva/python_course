class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def info(self):
        print(f"This is a {self.species}, its name is {self.name}")


pet1 = Pet('cat', 'Mura')
pet2 = Pet('dog', 'Spark')
pet3 = Pet('snake', 'Hiss')

pet1.info()
pet2.info()
pet3.info()
