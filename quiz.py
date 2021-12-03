from abc import ABC, abstractmethod


class Quiz(ABC):
    inputString: str
    inputList: list[str]
    result: any

    def test(self, testAnswer):
        text = open("test.txt", "r")
        self.inputList = text.read().split("\n")
        self.solve()
        print("Test Answer:", self.result, "real Answer:", testAnswer)
        assert self.result == testAnswer

        text = open("input.txt", "r")
        self.inputList = text.read().split("\n")

    def setInput(self, inputString: str) -> None:
        self.inputString = inputString

    @abstractmethod
    def solve(self) -> None:
        pass
