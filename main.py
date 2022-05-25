# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from dotenv import load_dotenv

from base import create_game
from statistic_game import statistic_game

load_dotenv()


def init_game():
    statistics = []
    simulation_limit = int(os.getenv('SIMULATIOS'))
    for i in range(simulation_limit):
        game = create_game()
        while not game.finish:
            for p in game.players:
                if p.out:
                    game.players.remove(p)
                game.start(p, game)
            game.rounds += 1
            if game.players.__len__() == 1 or game.rounds > int(os.getenv('LIMIT_RODADAS')):
                game.finish = True
                game.type_player = game.players[0].type_player if not game.rounds > int(os.getenv('LIMIT_RODADAS')) else None
        statistics.append(game.finish_game())
    statistic_game(statistics)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
