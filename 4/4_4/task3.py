"""
Вспомним нашего приятеля из предыдущих уроков: класс Vector.
Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
    1)  конструктор __init__, принимающий произвольное количество аргументов.
        Среди всех переданных аргументов необходимо оставить только целые числа
        и сохранить их в атрибут values в виде списка. Причем значения должны храниться в порядке неубывания.
        В случае, если целых чисел не передано, нужно в атрибут values сохранять пустой список;

    2)  переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
            - "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой.
               При этом значения должны быть упорядочены по возрастанию;
            - "Пустой вектор", если наш вектор не хранит в себе значения

    3)  переопределить метод __add__ так, чтобы экземпляр класса Vector мог складыватьс
            - с целым числом, в результате должен получиться новый Vector,
              у которого каждый элемент атрибута values увеличен на число
            - с другим вектором такой же длины. В результате должен получиться новый Vector,
              состоящий из суммы элементов, расположенных на одинаковых местах.
              Если длины векторов различаются, выведите сообщение "Сложение векторов разной длины недопустимо";
            - В случае, если вектор складывается с другим типом(не числом и не вектором),
              нужно вывести сообщение "Вектор нельзя сложить с <значением>"

    4)  переопределить метод __mul__ так, чтобы экземпляр класса Vector мог умножаться
            - на целое число. В результате должен получиться новый Vector,
              у которого каждый элемент атрибута values умножен на переданное число;
            - на другой вектор такой же длины. В результате должен получиться новый Vector,
              состоящий из произведения элементов, расположенных на одинаковых местах.
              Если длины векторов различаются, выведите сообщение "Умножение векторов разной длины недопустимо";
            - В случае, если вектор умножается с другим типом(не числом и не вектором),
              нужно вывести сообщение "Вектор нельзя умножать с <значением>";
"""


class Vector:
    def __init__(self, *args):
        # Оставляем только целые числа и сортируем их
        self.values = sorted(x for x in args if isinstance(x, int))

    def __str__(self):
        # Форматируем строковое представление вектора
        if self.values:
            return f"Вектор({', '.join(map(str, self.values))})"
        else:
            return "Пустой вектор"

    def __add__(self, other):
        # Сложение с целым числом
        if isinstance(other, int):
            return Vector(*(x + other for x in self.values))

        # Сложение с другим вектором
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "Сложение векторов разной длины недопустимо"
            return Vector(*(x + y for x, y in zip(self.values, other.values)))

        # Обработка неподходящего типа
        else:
            return f"Вектор нельзя сложить с {other}"

    def __mul__(self, other):
        # Умножение на целое число
        if isinstance(other, int):
            return Vector(*(x * other for x in self.values))

        # Умножение на другой вектор
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "Умножение векторов разной длины недопустимо"
            return Vector(*(x * y for x, y in zip(self.values, other.values)))

        # Обработка неподходящего типа
        else:
            return f"Вектор нельзя умножать с {other}"


# Пример использования
if __name__ == "__main__":
    v1 = Vector(1, 2, 3, 4)
    v2 = Vector(5, 6, 7, 8)

    print(v1)  # Вектор(1, 2, 3, 4)
    print(v2)  # Вектор(5, 6, 7, 8)

    # Сложение с целым числом
    v3 = v1 + 10
    print(v3)  # Вектор(11, 12, 13, 14)

    # Сложение с другим вектором
    v4 = v1 + v2
    print(v4)  # Вектор(6, 8, 10, 12)

    # Умножение на целое число
    v5 = v1 * 2
    print(v5)  # Вектор(2, 4, 6, 8)

    # Умножение на другой вектор
    v6 = v1 * v2
    print(v6)  # Вектор(5, 12, 21, 32)

    # Примеры с неподходящими типами
    v7 = Vector(1.5, 'a', 3)
    print(v7)  # Вектор(3)

    print(v1 + 'string')  # Вектор нельзя сложить с string
    print(v1 * 'string')  # Вектор нельзя умножать с string

    # Проверка на разную длину
    v10 = Vector(1, 2, 3)
    v11 = Vector(4, 5)
    print(v10 + v11)  # Сложение векторов разной длины недопустимо
    print(v10 * v11)  # Умножение векторов разной длины недопустимо
