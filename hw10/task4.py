class Ticket:
    def __init__(self, price, seat_number, destination):
        self.price = price
        self.destination = destination
        self.seat_number = seat_number


class Passenger:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.tickets_are_bought = False

    def info(self, ticket):
        print(f"{self.name} wants to buy a ticket to {ticket.destination}")

    def buy_ticket(self, ticket):
        if self.money >= ticket.price:
            self.tickets_are_bought = True
            print(f"{self.name} has bought a ticket to {ticket.destination}")
        else:
            print(f"{self.name} doesn't have enough money to complete the purchase")


passenger1 = Passenger('Anna', 1000)
ticket1 = Ticket(127, 24, "Novosibirsk")
ticket2 = Ticket(6455, 745, "Moscow")

passenger1.info(ticket1)
passenger1.buy_ticket(ticket1)
passenger1.info(ticket2)
passenger1.buy_ticket(ticket2)
