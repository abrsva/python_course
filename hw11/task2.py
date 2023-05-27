class Figure:
    def __init__(self, size):
        self.color = "white"
        self.size = size

    def info(self):
        pass

    def change_color(self, new_color):
        self.color = new_color


class Oval(Figure):
    def __init__(self, size):
        super().__init__(size)

    def info(self):
        print(f"This is an oval, its color is {self.color} and its size is {self.size}")


class Square(Figure):
    def __init__(self, size):
        super().__init__(size)

    def info(self):
        print(f"This is a square, its color is {self.color} and its size is {self.size}")


oval = Oval(36)
square = Square(85)

oval.info()
square.info()

oval.change_color('grey')
square.change_color('orange')

oval.info()
square.info()
