class AntilexicographicOrder:

    def __init__(self, n: int) -> None:
        self.p: list = [i for i in range(1, n+1)]
        self.__antylex(n)

    def __reverse(self, m: int) -> None:
        i: int = 0
        j: int = m - 1
        while i < j:
            self.p[i], self.p[j] = self.p[j], self.p[i]
            i += 1
            j -= 1

    def __antylex(self, m: int) -> None:
        if m == 1:
            print('(', end='')
            print(*self.p, end='')
            print(')')
        else:
            for i in range(m):
                self.__antylex(m - 1)
                if i < m:
                    self.p[i], self.p[m - 1] = self.p[m - 1], self.p[i]
                    self.__reverse(m - 1)
