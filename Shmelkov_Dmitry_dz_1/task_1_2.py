list_num = []
# task a
for num in range(100):
    if num % 2 > 0:
        num_cube = num ** 3
        sum_numbers = 0
        for i in str(num_cube):
            sum_numbers = sum_numbers + int(i)
        if sum_numbers % 7 == 0:
            list_num.append(num_cube)

print(list_num)

list_num = []
# task b
for num in range(100):
    if num % 2 > 0:
        num_cube = num ** 3 + 17
        sum_numbers = 0
        for i in str(num_cube):
            sum_numbers = sum_numbers + int(i)
        if sum_numbers % 7 == 0:
            list_num.append(num_cube)

print(list_num)
