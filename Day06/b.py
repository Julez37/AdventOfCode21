from helper.quiz import Quiz


class Day(Quiz):

    def tick(self, fishDict):
        newFishDict = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        for age in fishDict.keys():
            if age == 0:
                newFishDict[8] += fishDict[age]
                newFishDict[6] += fishDict[age]
            else:
                newFishDict[age - 1] += fishDict[age]
        return newFishDict


    def solve(self) -> None:
        lanternfish = [int(x) for x in self.inputList[0].split(",")]
        days = 256
        fishDict = {}
        for fish in lanternfish:
            if fish not in fishDict:
                fishDict[fish] = 0
            fishDict[fish] += 1

        for i in range(days):
            fishDict = self.tick(fishDict)

        self.result = sum(fishDict.values())

