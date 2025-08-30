class Checker:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self) -> str:
        return self.__color__
    
    def set_color(self, color: str):
        self.__color__= color