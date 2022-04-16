class Cell:
    def __init__(self, fill):
        self.fill = fill

    def __add__(self, other):
        return Cell(self.fill + other.fill)

    def __sub__(self, other):
        if self.fill > other.fill >= 0:
            return Cell(self.fill - other.fill)
        else:
            return print('Ошибка значения')

    def __mul__(self, other):
        return Cell(self.fill * other.fill)

    def __floordiv__(self, other):
        return Cell(self.fill // other.fill)

    def __truediv__(self, other):
        return Cell(self.fill // other.fill)

    def make_order(self, n):
        for _ in range(self.fill // n):
            print('*' * n)
        print('*' * (self.fill % n))


a = Cell(12)
b = Cell(15)
c = Cell(5)

print((a + b).fill)
print(a - b)
print((a - c).fill)
print((a * b).fill, type(a * b))
print((a / c).fill, type(a / c))
print((a // c).fill, type(a / c))

a.make_order(5)
