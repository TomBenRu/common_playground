from abc import ABC, abstractmethod


def zwei_hoch():
    res = 1
    while True:
        yield res
        res = res * 2


class Generator:
    def __init__(self, *args):
        print(args)
        self.args = args
        self.__value = 1

    def __zwei_hoch(self):
        self.__value = self.__value * 2

    def next(self):
        a = self.__yield()
        self.__zwei_hoch()
        return a

    def __yield(self):
        return self.__value

gg = zwei_hoch()
g = Generator(1, 2, 'drei')

for _ in range(11):
    print(next(gg))

for _ in range(11):
    print(g.next())
