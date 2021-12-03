from quiz import Quiz


class Day(Quiz):

    def solve(self) -> None:
        countOnes = [0] * len(self.inputList[0])
        for line in self.inputList:
            for i, bit in enumerate(line):
                countOnes[i] += int(bit)
        countOnes.reverse()
        gammaRateList = [1 * 2 ** i if x > (len(self.inputList) / 2) else 0 for i, x in enumerate(countOnes)]
        gammaRate = sum(gammaRateList)
        epsilonRate = gammaRate ^ (2 ** (len(self.inputList[0]))) - 1
        self.result = gammaRate * epsilonRate
