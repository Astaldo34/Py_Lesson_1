src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
tmp = src[0]
res = []
for item in src:
    if item > tmp:
        res.append(item)
    tmp = item

print(res)

result = (num for num in src if num > src[src.index(num) - 1])
print([*result][1:])
