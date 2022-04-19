class Zero:
    def __init__(self, x, y):
        try:
            print(x / y)
        except ZeroDivisionError:
            print('Деление на 0 недопустимо')

obj = Zero(13,2)
obj_2 = Zero(13,0)
