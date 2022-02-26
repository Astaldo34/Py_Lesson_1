price_list = [57.8, 46.51, 97, 12.01, 81.7, 54.2, 1.1, 2.2, 3.03, 4.04]
for item in sorted(price_list):
    price = round(float(item), 2)
    price_sep = str(price).split('.')
    if len(price_sep[1]) == 1:
        print(f'{price_sep[0]} руб {price_sep[1]}0 коп')
    else:
        print(f'{price_sep[0]} руб {price_sep[1]} коп')

price_list_up = sorted(price_list)
print('одинаковые - ', price_list[2], id(price_list[2]))
print('одинаковые - ', price_list_up[9], id(price_list_up[9]))

price_list_lower = sorted(price_list, reverse=True)
print(price_list_lower)

# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(price_list_lower[:5])

for item in price_list_lower[:5]:
    price = round(float(item), 2)
    price_sep = str(price).split('.')
    if len(price_sep[1]) == 1:
        print(f'{price_sep[0]} руб {price_sep[1]}0 коп')
    else:
        print(f'{price_sep[0]} руб {price_sep[1]} коп')
