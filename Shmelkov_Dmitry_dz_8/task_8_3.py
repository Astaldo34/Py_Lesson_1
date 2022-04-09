def type_logger(func):
    def wrapper(num):
        print(f'{func.__name__} {num}: {type(num)}')
        return func(num)

    return wrapper

@type_logger
def calc_cube(n):
    return n**3

print(calc_cube(7))
print(calc_cube(5))