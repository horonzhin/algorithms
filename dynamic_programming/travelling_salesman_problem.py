# Travelling Salesman Problem (Проблема коммивояжера)
# Есть набор городов, нужно найти *кратчайшие* и *быстрые* маршруты между городами с *минимальными затратами* на дорогу,
# чтобы посетить каждый город лишь раз и вернуться в начало.
#
# Используя грубую силу, можно с помощью перестановок перебрать все варианты и выбрать самые дешевые, тогда мы получим
# для n городов факториальное (n-1)! возможностей. Это означает, что для 10 городов есть 180 000 вариантов.
#
# Что нужно сделать для оптимизации:
# 1. Город № 1 отправная и конечная точка
# 2. Сгенерировать все перестановки городов (n-1)!
# 3. Рассчитать стоимость каждой перестановки и следить за минимальной
# 4. Вернуть перестановку с минимальной стоимостью
#
# Для это разобьем нашу проблему на множество небольших проблем и будем решать и постепенно.
# Сложность O(n^2 * 2^n), где вспомогательное пространство O(n^2), n - это кол-во городов.

from itertools import permutations
peaks = 4  # кол-во вершин (городов)


def travel_salesman_problem(graph, s):
    """
    Travelling Salesman Problem (Проблема коммивояжера)
    graph: матрица 4х4
    s: счетчик для вычисления суммы пройденного пути
    Сложность O(n^2 * 2^n), где вспомогательное пространство O(n^2), n - это кол-во городов.
    """
    vertex = []  # список для хранения вершин, наилучший маршрут для строк на графике
    for i in range(peaks):
        if i != s:  # если индекс не равен 0, добавляем его в список вершин. Покажет в каком направлении мы двигаемся
            vertex.append(i)
            print(vertex)

    min_path = []  # список минимального пути. Наименьшая комбинация вершин в графике.
    next_permutation = permutations(vertex)  # даст все комбинации для 1, 2 и 3. 6 перестановок.

    for i in next_permutation:  # перебираем все комбинации
        current_path_weight = 0  # счетчик

        k = s  # переназначим s и k будет представлять строку на графике
        for j in i:  # формируем столбцы
            current_path_weight += graph[k][j]  # вычисление всех путей и сложение их вместе
            print(j, i, current_path_weight, graph[k][j])
            k = j
        current_path_weight += graph[k][s]  # складываем суммы в графике с текущим путем
        min_path.append(current_path_weight)  # добавим к минимальному пути
        x = sorted(min_path)  # отсортируем пути

    return x[0]  # возвращаем первое минимальное число в списке - кратчайший маршрут


if __name__ == "__main__":
    graph = [[0, 10, 15, 20],  # А, A-B, A-C, A-D расстояния между городами
             [10, 0, 35, 25],  # B-A, B, B-C, B-D
             [15, 35, 0, 30],  # C-А, C-B, C, C-D
             [20, 25, 30, 0]]  # D-А, D-B, D-C, D
    s = 0
    print('Кратчайший маршрут:', travel_salesman_problem(graph, s))
