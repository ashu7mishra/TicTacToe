from cells import Cell


class Board:

    def __init__(self, dimension):
        self.__board = []
        for i in range(dimension):
            self.__board.append([])
            for j in range(dimension):
                self.__board[i].append(Cell(i, j))

    def displayBoard(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                if self.__board[i][j].getCellstate() == 1:
                    print("|   |")
                else:
                    print("| " + self.__board[i][j].getPlayer().getSymbol() + " |")
            print("\n")

    def getBoard(self):
        return self.__board

    def setBoard(self, board):
        self.__board = board
