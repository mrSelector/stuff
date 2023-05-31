class MyRange:
    def __init__(self, start, end=None, step=1):
        if end:
            self.start = start
            self.end = end
        else:
            self.start = 0
            self.end = start
        if step == 0:
            raise ValueError('bred')
        self.step = step

    def __getitem__(self, item):
        result = item * self.step + self.start
        if result >= self.end and self.step > 0 or \
                result <= self.end and self.step < 0:
            raise IndexError
        return result


r = MyRange(10, 2, -2)
print(r[2])

