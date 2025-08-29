class Player:
    def __init__(self, name):
        self.__name__ = name
        self.__checkers__ = 15

    def __str__(self):
        return f"Jugador: {self.__name__}, Fichas: {self.__checkers__}"