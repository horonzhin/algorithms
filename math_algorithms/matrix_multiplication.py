# Matrix multiplication — умножение матриц.
# Базовый алгоритм, который широко применяется в различных численных методах,
# и в частности в алгоритмах машинного обучения.
# Перемножение матриц (каждый элемент строки умножить на каждый элемент столбца, а затем сложить результаты).

import numpy as np


def matrix_multi_iteration(x, y):
    """Умножение матриц 2x2 при помощи итерации. Сложность O(n^3)"""
    result = [[0, 0],
              [0, 0]]
    for i in range(len(x)):  # итерируемся по строкам матрицы x
        for j in range(len(y[0])):  # итерируемся по столбцам матрицы y
            for k in range(len(y)):  # итерируемся по строкам матрицы y
                result[i][j] += x[i][k] * y[k][j]
    return result


def matrix_multi_strassen_iteration(x, y):
    """Алгоритм Штрассена с использованием итерации. Сложность О(n^2.8074)"""
    # разбиваем матрицы на четверти, берем каждый отдельный элемент
    a, b, c, d = x[0, 0], x[0, 1], x[1, 0], x[1, 1]
    e, f, g, h = y[0, 0], y[0, 1], y[1, 0], y[1, 1]

    # далее используем формулу
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)

    # вместо создания результирующей матрицы из 0 используем функцию создания массива от numpy
    return np.array([[c1, c2], [c3, c4]])


def matrix_multi_strassen_recursion(x, y):
    """
    Алгоритм Штрассена с использованием рекурсии.
    Рекурсией разбиваем матрицы по элементам и рекурсивно вычисляем 7 проходов.
    Сложность О(n^2.8074)
    """
    if len(x) == 1:
        return x * y

    # разбиваем матрицы на четверти, берем каждый отдельный элемент
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # далее используем формулу
    p1 = matrix_multi_strassen_recursion(a, f - h)
    p2 = matrix_multi_strassen_recursion(a + b, h)
    p3 = matrix_multi_strassen_recursion(c + d, e)
    p4 = matrix_multi_strassen_recursion(d, g - e)
    p5 = matrix_multi_strassen_recursion(a + d, e + h)
    p6 = matrix_multi_strassen_recursion(b - d, g + h)
    p7 = matrix_multi_strassen_recursion(a - c, e + f)

    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)

    # вместо создания результирующей матрицы из 0 используем функцию слияния четвертей
    # по горизонтали и вертикали в одну матрицу от numpy
    c = np.vstack((np.hstack((c1, c2)), np.hstack((c3, c4))))

    return c


def split(matrix):
    """Разбиение матрицы на четверти (по элементам)"""
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]


if __name__ == '__main__':
    x = np.array([[1, 2], [2, 3]])
    y = np.array([[2, 3], [3, 4]])

    # for end in matrix_multi_iteration(x, y):  # в итоге 8 умножений
    #     print(end)

    # print(matrix_multi_strassen_iteration(x, y))  # в итоге 7 умножений
    print(matrix_multi_strassen_recursion(x, y))  # в итоге 7 умножений
