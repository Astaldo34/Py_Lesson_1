class Date:
    def __init__(self, date):
        pass

    @classmethod
    def str_to_int(cls, str):
        res = []
        for i in str.split('-'):
            res.append(int(i))

        print(f'Число - {res[0]}')
        print(f'Месяц - {res[1]}')
        print(f'Год - {res[2]}')

    @staticmethod
    def valid_date(str):
        res = []
        for i in str.split('-'):
            res.append(int(i))

        try:
            if res[0] > 31:
                print('!!! Не верно указано число')
        except Exception:
            print('!!! Не указано число')

        try:
            if res[1] > 12:
                print('!!! Не верно указан месяц')
        except Exception:
            print('!!! Не указан месяц')

        try:
            if res[2] > 2022:
                print('!!! Не верно указан год')
        except Exception:
            print('!!! Не указан год')



obj_1 = Date('20-08-1985')
obj_1.str_to_int('40-08-3000')
Date.valid_date('40-08-3000')