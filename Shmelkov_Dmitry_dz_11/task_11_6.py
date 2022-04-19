class Storage:
    length = 100
    width = 100
    height = 20


class OfficeEqp:
    all_amount = 0

    @staticmethod
    def add_tmc(q):
        OfficeEqp.all_amount += q


class Printer(OfficeEqp):
    q_printer = 0

    def __init__(self, color):
        self.color = color

    def add_printer(self, q):
        if str(q).isnumeric():
            Printer.q_printer += q
            self.add_tmc(q)
            print(f'Добавлено {q} принтеров на склад')
        else:
            print('Не верный тип данных')



class Xerox(OfficeEqp):
    q_xerox = 0

    def __init__(self, color):
        self.color = color

    def add_xerox(self, q):
        Xerox.q_xerox += q
        self.add_tmc(q)


obj = OfficeEqp()
print(obj.all_amount)

obj_printer = Printer('black')
obj_xerox = Xerox('red')

obj_printer.add_printer(4)
obj_xerox.add_xerox(2)
obj_printer.add_printer('три')
print(obj.all_amount)
