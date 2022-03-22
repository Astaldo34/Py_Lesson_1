tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def func_gen(num):
    for n in range(num):
        if n > len(klasses) - 1:
            klasses.append('None')
        yield tuple([tutors[n], klasses[n]])


res_gen = func_gen(len(tutors))
print(type(res_gen), *res_gen)
# print(res_gen.__next__(), res_gen.__next__(), res_gen.__next__(), res_gen.__next__(), res_gen.__next__(),
#       res_gen.__next__(), res_gen.__next__(), res_gen.__next__())
