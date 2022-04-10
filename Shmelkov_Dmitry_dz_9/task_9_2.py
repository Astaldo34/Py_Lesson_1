class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        # print(self._length, self._width)

    def mass_calculation(self):
        print(self._length * self._width * 25 * 5)


Road(100,7).mass_calculation()