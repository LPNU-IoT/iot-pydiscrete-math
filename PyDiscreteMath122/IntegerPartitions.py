class IntegerPartitions:
    __d: int
    __S: list = []
    __R: list = []

    def __init__(self, n):
        self.__R = [0 for _ in range(n)]
        self.__S = [0 for _ in range(n)]

    def part(self, n) -> None:
        self.__S[0] = n
        self.__R[0] = 1
        self.__d = 1
        print(n)
        while self.__S[0] > 1:
            sum: int = 0
            if self.__S[self.__d - 1] == 1:
                sum = sum + self.__R[self.__d - 1]
                self.__d = self.__d - 1
            sum = sum + self.__S[self.__d - 1]
            self.__R[self.__d - 1] = self.__R[self.__d - 1] - 1
            l: int = self.__S[self.__d - 1] - 1
            if self.__R[self.__d - 1] > 0:
                self.__d = self.__d + 1
            self.__S[self.__d - 1] = l
            self.__R[self.__d - 1] = sum // l
            l = sum % l
            if l != 0:
                self.__d = self.__d + 1
                self.__S[self.__d - 1] = l
                self.__R[self.__d - 1] = 1
            self.__print(self.__d)

    def __print(self, d):
        for i in range(d):
            for j in range(self.__R[i]):
                print(f'{self.__S[i]}\t', end='')
        print()
