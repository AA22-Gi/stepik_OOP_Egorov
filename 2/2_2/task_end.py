"""
В вашем распоряжении класс Person, у которого имеется 7 атрибутов.

Программа будет принимать на вход произвольное количество слов в одну строку, разделенных пробелом.
Ваша задача проверить, является ли каждое из введенных слов названием атрибута.
Регистр слов значения не имеет.

Нужно вывести в каждой отдельной строке введенные слова по порядку и напротив через дефис указать,
нашлось свойство с таким именем или нет (вывести YES или NO)
"""


class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


line = input()
line_list = line.split()

for i in line_list:
    if i.lower() in Person.__dict__:
        print(f'{i}-YES')
    else:
        print(f'{i}-NO')
