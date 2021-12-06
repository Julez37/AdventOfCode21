from helper.quiz import Quiz


class Day(Quiz):

    def solve(self) -> None:
        pufferfish = [int(x) for x in self.inputList[0].split(",")]
        for i in range(80):
            pufferfish = [x - 1 for x in pufferfish]
            newFish = [8 for x in pufferfish if x == -1]
            pufferfish = [6 if x == -1 else x for x in pufferfish]
            pufferfish += newFish
        self.result = len(pufferfish)

