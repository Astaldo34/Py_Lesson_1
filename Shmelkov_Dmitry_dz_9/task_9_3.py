sot_worker = {"basic": '10000', "bonus": '5000'}

class Worker:
    name = 'Ork'
    surname = 'Horde'
    position  = 'slave'
    _income = sot_worker

class Position(Worker):
    def get_full_name(self):
        print(f'fullname - {self.name} {self.surname}')
    def get_total_income(self):
        total = int(self._income.get('basic')) + int(self._income.get('bonus'))
        print(f'total wage - {total}')


Position().get_full_name()
Position().get_total_income()