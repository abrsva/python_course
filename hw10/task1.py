class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.hungry = True

    def play(self):
        if not self.hungry:
            print(f"{self.name} is playing")
        else:
            print(f"{self.name} is angry")


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_cat(self, cat):
        cat.hungry = False


cat1 = Cat("Mura", 'Scottish')
human1 = Human("John", 20)

cat1.play()
human1.feed_cat(cat1)
cat1.play()
