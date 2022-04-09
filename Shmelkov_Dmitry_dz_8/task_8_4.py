from functools import wraps


def val_checker(l_func):
    def valid(func):
        @wraps(func)
        def wrapper(num):
            if l_func(num):
                res = func(num)
            else:
                raise ValueError(f'Не верное число {num}')
            return res

        return wrapper

    return valid


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(-5))
