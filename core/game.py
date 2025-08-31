from core.board import Board
from core.player import Player
from core.dice import Dice

class BackgammonGame:
    def __init__(self):

        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__players__ = [Player("Jugador 1"), Player("Jugador 2")]
        self.__turn__ = 0

    def get_board(self):
        return self.__board__

    def get_turn(self):
        return self.__turn__
    
    def set_turn(self, turn: int):
        self.__turn__ = turn

    def start(self):
        print("Bienvenido a Backgammon")
        self.__board__.setup_initial_positions()


    def roll_dice(self):

        return self.__dice__.roll()
    
    def next_turn(self):
        self.__turn__ = (self.__turn__ + 1) % 2

        return self.__players__[self.__turn__]
