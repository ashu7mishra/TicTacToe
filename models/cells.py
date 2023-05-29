from cellstate import CellState
from player import Player


class Cell:

    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__player = Player
        self.__cellstate = CellState

    def getRow(self):
        return self.__row

    def setRow(self, row):
        self.__row = row

    def getCol(self):
        return self.__col

    def setCol(self, col):
        self.__col = col

    def getPlayer(self):
        return self.__player

    def getCellstate(self):
        return self.__cellstate

