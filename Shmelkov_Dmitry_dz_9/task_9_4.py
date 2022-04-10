class Car:
    speed = 30
    color = 'red'
    name = 'basic'
    is_police = False

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скоровть машины {self.name} - {self.speed}')


class TownCar(Car):
    speed = 70
    color = 'black'
    name = 'town'
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена скорость! ({self.speed})')
        else:
            print(f'Скоровть машины {self.name} - {self.speed}')


class SportCar(Car):
    speed = 100
    color = 'yellow'
    name = 'sport'
    is_police = False


class WorkCar(Car):
    speed = 30
    color = 'grey'
    name = 'work'
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена скорость! ({self.speed})')
        else:
            print(f'Скоровть машины {self.name} - {self.speed}')


class PoliceCar(Car):
    speed = 100
    color = 'blue'
    name = 'police'
    is_police = True


car_1 = Car()
car_1.go()
car_1.show_speed()

police_1 = PoliceCar()
police_1.go()
police_1.show_speed()

town_1 = TownCar()
town_1.go()
town_1.show_speed()