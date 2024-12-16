"""
Ваша задача - реализовать класс, который принимает обозначение цвета палитры в формате HEX
в виде строки и может перевести его в формат RGB при помощи свойств red, green, blue.

Ознакомиться с форматом HEX и RGB вы можете самостоятельно в следующей статье.

Для решения данной задачи напишите только реализацию класса Colour.
"""


class Colour:
    def __init__(self, hex_colour):
        # Убедимся, что HEX начинается с '#'
        if hex_colour.startswith('#'):
            hex_colour = hex_colour[1:]
        if len(hex_colour) != 6:
            raise ValueError("Некорректный формат HEX. Должно быть 6 символов.")

        # Преобразуем HEX в RGB
        self._red = int(hex_colour[0:2], 16)
        self._green = int(hex_colour[2:4], 16)
        self._blue = int(hex_colour[4:6], 16)

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue


if __name__ == '__main__':
    colour = Colour("#ff0000")
    print(colour.red)
    print(colour.green)
    print(colour.blue)
    print()

    colour = Colour("#00ff2d")
    print(colour.red)
    print(colour.green)
    print(colour.blue)
    print()

    colour = Colour("#aacce4")
    print(colour.red)
    print(colour.green)
    print(colour.blue)
