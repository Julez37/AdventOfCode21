from helper.quiz import Quiz
import re


class Day(Quiz):

    def getLinePoints(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        pointList = []
        if dy == 0:
            for x in range(min([x1, x2]), max([x1, x2]) + 1):
                pointList.append((x, y1))
        elif dx == 0:
            for y in range(min([y1, y2]), max([y1, y2]) + 1):
                pointList.append((x1, y))
        return pointList

    def solve(self) -> None:
        fields = {}
        pattern = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)$")
        count = 0
        for lineString in self.inputList:
            line = re.match(pattern, lineString)
            x1, y1, x2, y2 = [int(x) for x in line.groups()]
            linePoints = self.getLinePoints(x1, y1, x2, y2)
            for point in linePoints:
                if point not in fields:
                    fields[point] = 0
                fields[point] += 1
        for value in fields.values():
            if value >= 2:
                count += 1
        self.result = count


