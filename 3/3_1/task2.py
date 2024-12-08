"""
Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.

В классе Counter нужно определить:
    Метод start_from, который принимает один необязательный аргумент — значение,
    с которого начинается подсчет (по умолчанию равно 0);

    Метод increment, который увеличивает счетчик на 1;

    Метод display, который печатает фразу «Текущее значение счетчика = <value>»;

    Метод reset,  который обнуляет накопившееся значение счетчика.
Необходимо написать только определение класса Counter.
"""


class Counter:
    def start_from(self, count: int = 0):
        self.count = count

    def increment(self):
        self.count += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.count}')

    def reset(self):
        self.count = 0


if __name__ == '__main__':
    c1 = Counter()

    c1.start_from(45)
    c1.display()  # печатает 45
    c1.increment()
    c1.display()  # печатает 46
    c1.increment()
    c1.display()  # печатает 47
    c1.reset()  # обнулили с1
    c1.display()  # печатает 0
