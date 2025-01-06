"""
Создайте дескриптор MaxLengthAttribute, который возвращает имя самого длинного атрибута в экземпляре.

Если несколько атрибутов имеют одинаковую длину, необходимо вернуть значение,
стоящее последним по лексикографическому порядку без учета регистра букв.

Если у экземпляра отсутствуют свои собственные атрибуты, необходимо вернуть None.
задача написать только определение класса MaxLengthAttribute
"""


class MaxLengthAttribute:
    def __get__(self, instance, owner):
        if instance is None:
            return self

        # Получаем все атрибуты экземпляра
        attributes = {key: value for key, value in instance.__dict__.items() if not key.startswith('__')}

        if not attributes:
            return None

        # Находим атрибут с максимальной длиной
        max_length = 0
        max_length_attr = None

        for key in attributes.keys():
            key_length = len(key)
            if key_length > max_length or (key_length == max_length and key.lower() > max_length_attr.lower()):
                max_length = key_length
                max_length_attr = key

        return max_length_attr


if __name__ == '__main__':
    class MyClass:
        max_length_attribute = MaxLengthAttribute()


    obj = MyClass()
    obj.name = "Vasiliy"
    obj.city = "Saint Peterburg"
    obj.country = "Rus"
    print(obj.max_length_attribute)


    class MyClass:
        max_length_attribute = MaxLengthAttribute()


    obj = MyClass()
    print(obj.max_length_attribute)


    class JustClass:
        max_atr = MaxLengthAttribute()


    obj = JustClass()
    obj.mock = 15
    obj.city = "Saint Peterburg"
    obj.name = "Vasiliy"
    obj.door = 'wood'

    print(obj.max_atr)
