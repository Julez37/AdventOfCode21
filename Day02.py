import re

from quiz import Quiz


class Day(Quiz):

    def solve(self) -> None:
        pos = [0, 0, 0]
        commands = ["forward", "backward", "down", "up"]
        pattern = re.compile(r"(\w+) (\d+)")
        for line in self.inputList:
            result = re.match(pattern, line)
            i = commands.index(result.groups()[0])
            pos[i // 2] += int(result.groups()[1]) * ((-1) ** i)
            if i == 0:
                pos[2] += (int(result.groups()[1]) * pos[1])
        self.result = pos[0] * pos[2]

