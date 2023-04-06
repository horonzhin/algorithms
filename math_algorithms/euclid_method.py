def greatest_common_divisor_recursion(a, b):
    """
    Метод Евклида
    Поиск наибольшего общего делителя двух целых положительных чисел
    (наибольшее целое число, которое делит каждое из них без остатка) с помощью алгоритма Евклида:
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor_recursion(b, a % b)


if __name__ == '__main__':
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    print(f'Наибольший общий делитель для {a} и {b}: {greatest_common_divisor_recursion(a, b)}')

