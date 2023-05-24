class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):

    def __init__(self, l, w, h):
        super().__init__(l, w, h)
        self.places = None

    def how_places(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def out_places(self):
        print(self.places)


class Cabinet(Table):

    def suits_for_work(self):
        if self.height >= 100 and self.width >= 80:
            print("The table suits for work")
        else:
            print("The table doesn't suit for work")

    def has_place_for_computer(self):
        square = self.long * self.width
        if square >= 3500:
            print("A computer can be placed at the table")
        else:
            print("A computer can't be placed at the table")
