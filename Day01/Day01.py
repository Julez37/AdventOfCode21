from helper.quiz import Quiz


class Day01(Quiz):

    def solve(self) -> None:
        countDeeper = 0
        currentValue = (2 ** 32)
        depths = []
        for string in self.inputList:
            depths.append(int(string))

        for i in range(len(depths) - 2):
            depthValue = depths[i] + depths[i + 1] + depths[i + 2]
            if depthValue > currentValue:
                countDeeper += 1
            currentValue = depthValue
        self.result = countDeeper
