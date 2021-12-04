import re


class BingoBoard:

    def __init__(self):
        self.board = []
        self.won = False

    def fill(self, inputList):
        for line in inputList:
            numbers = re.split(r"\s+", line.strip())
            row = []
            self.board.append(row)
            for number in numbers:
                row.append([int(number), False])

    def checkNumber(self, number):
        for row in self.board:
            for field in row:
                if field[0] == number:
                    field[1] = True
        if not self.won and self.checkIfFinished():
            self.won = True
            return True
        return False

    def checkIfFinished(self) -> bool:
        for row in self.board:
            checked = [x for x in row if x[1]]
            if len(checked) == len(row):
                return True

        for i, col in enumerate(self.board[0]):
            checked = 0
            for row in self.board:
                if row[i][1]:
                    checked += 1
            if checked == len(self.board):
                return True

        return False

    def getFields(self, mark):
        result = []
        for row in self.board:
            for field in row:
                if field[1] == mark:
                    result.append(field[0])
        return result
