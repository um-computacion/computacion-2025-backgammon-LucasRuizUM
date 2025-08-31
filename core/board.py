from core.checker import Checker

class Board:
    def __init__(self):
        self.__points__ = [[] for _ in range(24)]

    def get_points(self):
        return self.__points__

    def setup_initial_positions(self):
          self.__points__[23] = [Checker("white") for _ in range(2)]  
          self.__points__[12] = [Checker("white") for _ in range(5)]  
          self.__points__[7]  = [Checker("white") for _ in range(3)]  
          self.__points__[5]  = [Checker("white") for _ in range(5)]   

       
          self.__points__[0]  = [Checker("black") for _ in range(2)]  
          self.__points__[11] = [Checker("black") for _ in range(5)]  
          self.__points__[16] = [Checker("black") for _ in range(3)] 
          self.__points__[18] = [Checker("black") for _ in range(5)]   

    def get_point(self, index: int):
        
        return self.__points__[index]