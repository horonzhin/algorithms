# Egyptian Fractions (Египетские дроби)
# Жадный алгоритм, который преобразует рациональные числа в египетские дроби.
# Египетские дроби - это представление рационального числа `4/5` в виде суммы различных единичных дробей
# (где числитель 1, а знаменатель любое целое число `1/2`, `1/3`).
# Например: `4/5 = 1/2 + 1/3` или `2/3 = 1/3 + 1/3`
#
# Задача: есть 7 пицц и 12 детей, чтобы все дети получили одинаковую долю,
# нужно 6 пицц разделить пополам `1/2` (получится 12 кусочков половины пиццы)
# и 1 пиццу разделить на 12 частей `1/12`. В итоге получается `1/2 + 1/12 = 7/12` (7 пицц на 12 детей).

import math


def egyptian_fractions(numerator, denominator):
    """Egyptian Fractions (Египетские дроби). Сложность O(d), где d - знаменатель входной дроби."""
    egypt_list = []  # список знаменателей
    while numerator != 0:  # пока числитель не равен 0
        x = math.ceil(denominator/numerator)  # округляем число в большую строну, важно когда есть float < 1
        egypt_list.append(x)  # записываем его в список знаменателей
        numerator = x * numerator - denominator  # переназначаем числитель
        denominator *= x  # переназначаем знаменатель так, что получим 2 и 12 - это наименьшие общие знаменатели
    string = ''
    for ones in egypt_list:
        string += f'1/{ones} + '  # добавим знаменатель под дробь при помощи f-строки
    final_string = string[:-3]  # отрежем последний плюс
    return final_string


if __name__ == '__main__':
    print(egyptian_fractions(7, 12))