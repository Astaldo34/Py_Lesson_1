import time

class TrafficLight:
    __color = 'red'

    def running(self):
        print(TrafficLight.__color)
        if TrafficLight.__color == 'red':
            time.sleep(7)
            TrafficLight.__color = 'yellow'
            print(TrafficLight.__color)
        if TrafficLight.__color == 'yellow':
            time.sleep(2)
            TrafficLight.__color = 'green'
            print(TrafficLight.__color)
        if TrafficLight.__color == 'green':
            time.sleep(5)
            TrafficLight.__color = 'red'
            print(TrafficLight.__color)


TrafficLight().running()
