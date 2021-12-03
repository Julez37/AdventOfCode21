from quiz import Quiz


class Day(Quiz):

    def solve(self) -> None:
        params = [0, 0]
        for j in range(2):

            currentList = self.inputList.copy()

            i = 0

            while len(currentList) > 1:
                count = 0
                for line in currentList:
                    count += int(line[i])
                bit = count >= (len(currentList) / 2)
                if j > 0:
                    bit = not bit
                currentList = [x for x in currentList if int(x[i]) == bit]
                i += 1

            paramValue = [int(x) * 2 ** i for i, x in enumerate(currentList[0][::-1])]
            params[j] = sum(paramValue)

        self.result = params[0] * params[1]


