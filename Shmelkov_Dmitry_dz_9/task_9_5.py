class Stationery:
    title = 'all'

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Запуск отрисовки ручкой')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Запуск отрисовки карандашом')



class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'Запуск отрисовки маркером')


test = Stationery()
test.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()