def thesaurus(*args):
    dict_names = {}
    for name in [*args]:
        if (dict_names.get(name[0])) != None:
            cure_value = [dict_names.get(name[0])]
            cure_value.append(name)
            dict_names[name[0]] = cure_value
            # dict_names[name[0]] = [dict_names.get(name[0])].append(name) # Не понимаю почему вот так возвращает None...
            # print(dict_names.get(name[0]))
        else:
            dict_names[name[0]] = name
    return print(dict_names)


thesaurus("Иван", "Мария", "Петр", "Илья", "Милана")
