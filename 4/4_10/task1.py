"""
Создайте класс AttributeChecker, который имеет:
    1)  магический метод __contains__,
        принимающий имя атрибута и возвращает True, если этот атрибут существует в экземпляре класса,
        и False в противном случае.
"""


class AttributeChecker:
    def __contains__(self, item):
        return item in self.__dict__


if __name__ == '__main__':
    # Тест 1: Проверка наличия отсутствующего атрибута
    check = AttributeChecker()
    assert "name" not in check
    assert "age" not in check
    setattr(check, 'name', 'Russell')
    check.age = 10
    # print(check.__dict__)

    # Тест 2: Проверка добавления атрибутов
    assert "name" in check
    assert "age" in check

    # Тест 3: Проверка атрибутов другого ЭК
    check_2 = AttributeChecker()
    assert "name" not in check_2
    assert "age" not in check_2

    # Тест 4: Проверка наличия атрибутов после удаления
    delattr(check, "name")
    assert "name" not in check
    assert "age" in check

    print("Good")
