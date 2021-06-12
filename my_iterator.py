class QuadraticNumberst:
    def __init__(self, a: int, b: int = 0, step: int = 1):
        if b:
            a, b = b, a
        self.from_ = b
        self.to = a
        self.current = self.from_
        self.step = step

    @staticmethod
    def operation(x: int) -> int:
        return x ** 2

    def __iter__(self):
        return self

    def __next__(self):
        old = self.current
        if old >= self.to:
            raise StopIteration
        else:
            self.current += self.step
            return self.operation(old)


for i in QuadraticNumberst(100, step=10):
    print(i)
