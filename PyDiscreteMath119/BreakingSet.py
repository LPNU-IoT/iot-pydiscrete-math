class BreakingSet:
    __set: list = [0]
    __block: list = [0]
    __next: list = [0]
    __previous: list = [0]
    __toward: list = [0]

    def sub_set(self, n: int) -> None:
        for i in range(1, n + 1):
            self.__set.append(i)
            self.__block.append(1)
            self.__toward.append(True)
            self.__next.append(0)
            self.__previous.append(0)
        self.__next[1] = 0
        self.__print(self.__set, self.__block, n)
        j: int = n
        while j > 1:
            k: int = self.__block[j]
            if self.__toward[j]:
                if self.__next[k] == 0:
                    self.__next[k] = j
                    self.__previous[j] = k
                    self.__next[j] = 0
                if self.__next[k] > j:
                    self.__previous[j] = k
                    self.__next[j] = self.__next[k]
                    self.__previous[self.__next[j]] = j
                    self.__next[k] = j
                self.__block[j] = self.__next[k]
            else:
                self.__block[j] = self.__previous[k]
                if k == j:
                    if self.__next[k] == 0:
                        self.__next[self.__previous[k]] = 0
                    else:
                        self.__next[self.__previous[k]] = self.__next[k]
                        self.__previous[self.__next[k]] = self.__previous[k]
            self.__print(self.__set, self.__block, n)
            j = n
            while (j > 1) and (
                    (self.__toward[j] and (self.__block[j] == j)) or (not self.__toward[j] and (self.__block[j] == 1))):
                self.__toward[j] = not self.__toward[j]
                j = j - 1

    def __print(self, a: list, b: list, n: int) -> None:
        sub_set: list = [*a]
        block: list = [*b]
        for k in range(1, n):
            for i in range(1, n - k + 1):
                if block[i] > block[i + 1]:
                    block[i], block[i + 1] = block[i + 1], block[i]
                    sub_set[i], sub_set[i + 1] = sub_set[i + 1], sub_set[i]
        print(f'({sub_set[1]}', end='')
        for i in range(2, n + 1):
            if block[i] != block[i - 1]:
                print(f') ({sub_set[i]}', end='')
            else:
                print(f'{sub_set[i]}', end='')
        print(')')
