class Figure:
    def __init__(self, color, size):
        self.color = color
        self.size = size


class Pyramid(Figure):
    def __init__(self, color, size):
        super().__init__(color, size)

    def info(self):
        print(f"This is a {self.size} {self.color} pyramid")


class Ball(Figure):
    def __init__(self, color, size):
        super().__init__(color, size)

    def info(self):
        print(f"This is a {self.size} {self.color} ball")


class Cube(Figure):
    def __init__(self, color, size):
        super().__init__(color, size)

    def info(self):
        print(f"This is a {self.size} {self.color} cube")


class Box:
    def __init__(self):
        self.figures = []

    def add_figure(self, figure):
        if isinstance(figure, Figure):
            self.figures.append(figure)

    def whats_inside(self):
        for figure in self.figures:
            figure.info()


ball1 = Ball("yellow", "big")
cube1 = Cube("red", "small")
pyramid1 = Pyramid("orange", "huge")

box1 = Box()
box1.add_figure(ball1)
box1.add_figure(cube1)
box1.add_figure(pyramid1)

box1.whats_inside()
