from playertype import PlayerType


class Player:

    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol
        self.__playertype = PlayerType

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSymbol(self):
        return self.__symbol

    def setSymbol(self, symbol):
        self.__symbol = symbol

    def getPlayerType(self):
        return self.__playertype

