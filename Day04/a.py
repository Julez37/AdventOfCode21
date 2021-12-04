from helper.quiz import Quiz
from math import ceil
from Day04.BingoField import BingoBoard

class Day(Quiz):

    def solve(self) -> None:
        numbersToCheck = [int(x) for x in self.inputList[0].split(",")]
        boards = []
        for i in range(0, ceil((len(self.inputList) - 2) / 6)):
            board = BingoBoard()
            board.fill(self.inputList[i*6+2:i*6+7])
            boards.append(board)

        for turn in numbersToCheck:
            for board in boards:
                if board.checkNumber(turn):
                    self.result = turn * sum(board.getFields(False))
                    return
