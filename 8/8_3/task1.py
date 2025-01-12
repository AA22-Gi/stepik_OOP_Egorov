"""
Прыжки в воду

Очень красивый и зрелищный вид спорта, где спортсмены показывают сколько сальто можно успеть сделать за один раз.

По правилам локальных соревнований каждый прыжок оценивается тремя судьями,
каждый из них должен выставить оценку - вещественное число от 0 до 10.
Затем находится среднее арифметическое по выставленным оценкам и умножается на коэффициент сложности прыжка,
в результате получим значение балла спортсмена.
Кто наберет самое большое количество баллов тот и победит на этих соревнованиях.

Перед вами имеется дата-класс Athlet, в котором хранятся имя спортсмена,
коэффициент его прыжка и выставленные оценки за исполнение.
from dataclasses import dataclass, field

@dataclass
class Athlet:
    name: str
    coefficient: float
    scores: list = field(default_factory=list)

Ваша задача дописать класс Athlet таким образом, чтобы его экземпляры могли сортироваться по баллам.
Это нужно для определения победителя соревнований
Примечание: так же обратите внимание на то, как спортсмен выводится в тестах.
"""

from dataclasses import dataclass, field

@dataclass
class Athlet:
    name: str
    coefficient: float
    scores: list = field(default_factory=list)

    def calculate_score(self) -> float:
        if not self.scores:
            return 0.0
        average_score = sum(self.scores) / len(self.scores)
        return average_score * self.coefficient

    def __lt__(self, other):
        return self.calculate_score() < other.calculate_score()

    def __repr__(self):
        return f"Athlet(name='{self.name}')"


if __name__ == '__main__':
    sportsmans = [
        Athlet('Иван', 1.5, [9.0, 8.0, 7.0]),
        Athlet('Кирилл', 1.6, [9.0, 8.0, 10.0]),
        Athlet('Петр', 1.0, [10.0, 9.0, 8.0]),
        Athlet('Аркадий', 1.1, [10.0, 9.5, 8.7]),
        Athlet('Алексей', 1.2, [8.0, 7.0, 6.0]),
        Athlet('Всеволод', 1.5, [8.0, 7.0, 7.0])
    ]

    print("Итоговая таблица")
    for i, sportsman in enumerate(sorted(sportsmans, reverse=True)):
        print(f"{i + 1}.{sportsman}")