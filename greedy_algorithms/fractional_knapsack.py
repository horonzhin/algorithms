# Fractional Knapsack (Дробный рюкзак)
# Есть несколько предметов, каждый предмет имеет стоимость value = [150, 100, 90, 140, 120] и
# вес weight = [30, 50, 10, 70, 40]. Нужно выбрать какие предметы принесут наибольшую прибыль.
# Предметы можно делить, если они делимые. Необходимо набить рюкзак самыми ценными предметами.
#
# Используя грубую силу: перебрав все возможные подмножества со всеми различными дробями.
# Мы получим сложность O(2^n). Жадный алгоритм сократит сложность до O(n log n).
#
# Идея в том, чтобы рассчитать соотношение веcа и стоимости `ratio = value / weight`,
# отсортировать результаты и добавлять от большего к меньшему.

def fractional_knapsack(value, weight, capacity):
    """Fractional Knapsack. Сложность O(n log n)"""
    items = list(range(len(value)))
    print(items, '- количество предметов')
    ratio = [v // w for v, w in zip(value, weight)]
    print(ratio, '- коэффициенты предметов')
    str_ratios = sorted(ratio, reverse=True)
    print(str_ratios, '- отсортированные коэффициенты по убыванию')
    items.sort(key=lambda i: ratio[i], reverse=True)  # позиции в индексе коэффициентов предметов
    print(items, '- соотношение позиций в индексе (1 список) с коэффициентами предметов (2 список)')

    max_value = 0
    fractions = [0] * len(value)  # список длины наших значений, который будем называть дробями

    for i in items:  # перебираем предметы
        if weight[i] <= capacity:  # если вес меньше вместительности
            fractions[i] = 1  # добавим 1 в список с дробями на свою позицию индекса
            max_value += value[i]  # добавим значение в max_value
            capacity -= weight[i]  # вычтем вес из нашей вместительности
        else:  # когда все сделали
            fractions[i] = capacity // weight[i]  # берем дробное значение последнего предмета
            max_value += value[i] * capacity // weight[i]  # и добавляем его к максимальному значению

    return print(max_value)


if __name__ == '__main__':
    weight = [30, 50, 10, 70, 40]
    value = [150, 100, 90, 140, 120]
    capacity = 150
    fractional_knapsack(value, weight, capacity)
