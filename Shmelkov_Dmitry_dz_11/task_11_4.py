class Storage:
    length = 100
    width = 100
    height = 20


class OfficeEqp:
    amount = 100


class Printer(OfficeEqp):
    def __init__(self, color):
        self.color = color


class Xerox(OfficeEqp):
    def __init__(self, color):
        self.color = color

