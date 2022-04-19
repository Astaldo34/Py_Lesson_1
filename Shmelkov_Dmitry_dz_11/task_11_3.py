class OnlyInt:
    def __init__(self):
        data = []
        str_n = ''
        print('Началось')
        while str_n != 'stop':
            str_n = input('Введите число: ')
            try:
                str_n = int(str_n)
                data.append(str_n)
            except Exception:
                if str_n == 'stop':
                    break
                print('Можно вводить только цифры!')

        print(f'Итоговый список - {data}')




obj = OnlyInt()


