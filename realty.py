from random import randint


class Realty:

    def __init__(self, number):
        self.number = number
        self.player = None
        self.rent = randint(20, 50)
        self.price = randint(50, 150)

    def __str__(self):
        return f"{self.number}"
