from itertools import zip_longest
import json

fio_array = []
hobby_array = []
with open('users.csv', 'r', encoding='utf=8') as fio:
    for line in fio:
        fio_array.append(line.replace('\n', '').replace(',', ' '))


with open('hobby.csv', 'r', encoding='utf=8') as hobby:
    for line in hobby:
        hobby_array.append(line.replace('\n', ''))

if len(hobby_array) > len(fio_array):
    print(1)
else:
    fio_hobby = dict(zip_longest(fio_array, hobby_array, fillvalue=None))
    print(fio_hobby)
    with open('fio_hobby.csv', 'w', encoding='utf=8') as f:
        json.dump(fio_hobby, f)
