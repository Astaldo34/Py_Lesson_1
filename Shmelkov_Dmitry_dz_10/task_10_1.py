m_1 = [[1, 2], [3, 4]]
m_2 = [[5, 6], [7, 8]]

class Matrix:
    def __init__(self, args):
        self.args = args
        pass

    def __str__(self):
        return '\n'.join(str(i) for i in self.args)

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(cur_obj, other_obj)]
                       for cur_obj, other_obj in zip(self.args, other.args)])

print(f'{Matrix(m_1)} \n')
print(f'{Matrix(m_2)} \n')
print(Matrix(m_1) + Matrix(m_2))