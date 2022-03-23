src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
res = []
for item in src:
    if src.count(item) == 1:
        res.append(item)

print(res)

# result = list(set(src))
# print(result)

result = []
tmp = set()

for el in src:
    if el not in tmp:
        result.append(el)
    elif el in result:
        result.remove(el)
    tmp.add(el)
print(list(result))
