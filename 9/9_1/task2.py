"""
Создайте перечисление Size, в котором хранятся размеры одежды:

S - small
M - medium
L - large
XL - extra large
XXL - extra extra large
В списке сперва указаны названия атрибутов, затем их строковые значения.

Ваша задача написать только определения класса Size
"""

from enum import Enum


class Size(Enum):
    S = 'small'
    M = 'medium'
    L = 'large'
    XL = 'extra large'
    XXL = 'extra extra large'
