list_name = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for index, item in enumerate(list_name):
    for i in item:
        if i == "+":
            list_name[index] = '"+05"'
    if item.isnumeric():
        print(item)
        if (len(item) < 2):
            list_name[index] = '0' + list_name[index]
        list_name[index] = '"' + list_name[index] + '"'

    # if item.isnumeric():
    #     print(isinstance(item, str))
    #     print(item)
    #     if (len(item) < 2):
    #         list_name[index] = '0' + list_name[index]
    #     list_name[index] = '"' + list_name[index] + '"'

print(list_name)
str_list = ' '.join(list_name)
print(str_list)

"""
Не понял как выявить число "+5"
"""
