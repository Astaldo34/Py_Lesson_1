def f_gen(n):
    for num in range(1, n, 2):
        yield num

gen_num = f_gen(100)
print(type(gen_num), gen_num)
print(*gen_num)