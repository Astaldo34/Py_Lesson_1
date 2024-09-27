list_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

for item in list_name:
    list_item = item.split(' ')
    print('Привет, ' + list_item.pop().title() + '!')