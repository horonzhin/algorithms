from check import timer, calls_counter


@timer
def gcd(a, b):
    """
    Поиск наибольшего общего делителя двух целых положительных чисел.
    Сложность O(min(a, b)), но если a и b будут большими числами понадобятся тысячи лет вычислений.
    """
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


@calls_counter
@timer
def gcd_rec(a, b):
    """
    Метод Евклида.
    Поиск наибольшего общего делителя двух целых положительных чисел.
    Сложность O(min(a, b)).
    Количество рекурсивных вызовов зависит от того, сколько раз выполняется операция остатка от деления.
    С большими числами этот алгоритм будет гораздо быстрее.
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input('Введите два числа через пробел: ').split())
    print(gcd(a, b))
    print(gcd_rec(a, b))
