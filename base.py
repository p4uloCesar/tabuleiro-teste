from abc import ABC
import os
from random import randint

from game import Game
from player import PlayerImpulsive, PlayerDemanding, PlayerCautious, PlayerRandom

type_player = {
    "impulsive": PlayerImpulsive,
    "demanding": PlayerDemanding,
    "cautious": PlayerCautious,
    "randomer": PlayerRandom,
}


def create_game():
    game = Game()
    game.players = [type_player[type_p](type_player=type_p) for type_p in os.getenv('TYPE_PLAYER').split(',')]
    return game
