import abc
import os
from abc import ABC
from random import randint

from dotenv import load_dotenv

from realty import Realty

load_dotenv()


class AbstractPlayer(ABC):

    def __init__(
            self, type_player, pos=0,
            balance=os.getenv('SALDO_INIT')
    ):
        self.pos = pos
        self.balance = float(balance)
        self.type_player = type_player
        self.out = False

    def __str__(self):
        return f"{self.type_player}"

    def buy(self, obj: Realty):
        self.balance -= obj.price
        obj.player = self
        if float(self.balance) <= 0:
            self.out = True

    def income(self, obj: Realty):
        self.balance -= obj.rent
        obj.player.balance += obj.rent
        if float(self.balance) <= 0:
            self.out = True

    @abc.abstractmethod
    def buy_or_income(self, obj: Realty):
        return self.balance


class PlayerImpulsive(AbstractPlayer):

    def buy_or_income(self, obj: Realty):
        super(PlayerImpulsive, self).buy_or_income(obj)
        if obj.player is not None:
            self.income(obj)
        else:
            self.buy(obj)


class PlayerDemanding(AbstractPlayer):

    def buy_or_income(self, obj: Realty):
        super(PlayerDemanding, self).buy_or_income(obj)
        if obj.player is not None:
            self.income(obj)
        elif obj.rent >= 50:
            self.buy(obj)


class PlayerCautious(AbstractPlayer):

    def buy_or_income(self, obj: Realty):
        super(PlayerCautious, self).buy_or_income(obj)
        if obj.player is not None:
            self.income(obj)
        elif (self.balance - obj.price) >= 80:
            self.buy(obj)


class PlayerRandom(AbstractPlayer):

    def buy_or_income(self, obj: Realty):
        super(PlayerRandom, self).buy_or_income(obj)
        if obj.player is not None:
            self.income(obj)
        elif randint(0, 1) > 0:
            self.buy(obj)
