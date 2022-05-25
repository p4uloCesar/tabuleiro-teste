import os
from random import randint

from dotenv import load_dotenv

from player import AbstractPlayer
from realty import Realty

load_dotenv()


class Game:

    def __init__(self, *args, **kwargs):
        self.finish = False
        self.rounds = 0
        self.type_player = None
        self.players = []
        self.realty = [Realty(number) for number in range(int(os.getenv('TOTAL_CASAS')))]

    def dice(self):
        return randint(1, 6)

    def go_to_position(self, player: AbstractPlayer):
        go_to_pos = player.pos + self.dice()
        if go_to_pos >= int(os.getenv('TOTAL_CASAS')):
            player.balance += float(os.getenv('SALDO_GANHO'))
            go_to_pos -= int(os.getenv('TOTAL_CASAS'))
        player.pos = go_to_pos
        return go_to_pos

    def start(self, player: AbstractPlayer, game):
        realty = self.realty[self.go_to_position(player)]
        player.buy_or_income(realty)

    def finish_game(self):
        return {
            "type_player": self.type_player,
            "rounds": self.rounds,
            "timeout": self.rounds > int(os.getenv('LIMIT_RODADAS')),
        }
