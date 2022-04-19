class ComplexNumbers:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        self.val += other
        return self

    def __mul__(self, other):
        self.val += other
        return self


obj = ComplexNumbers(complex(4, 3))
print(obj.val)
obj += complex(1, 2)
obj *= complex(1, 2)
print(obj.val)
