if __name__ == '__main__':

    # Перевод целых чисел в бинарные выражения
    num = int(input('Введите целое число: '))

    if num < 0:
        is_neg = True
        num = abs(num)
    else:
        is_neg = False
    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    if is_neg:
        result = '-' + result

    print('Бинарное выражение: ', result)

    # Перевести число с плавающей точкой в бинарное выражение
    x = float(input('Введите число с плавающей точкой от 0 до 1: '))

    p = 0
    while ((2 ** p) * x) % 1 != 0:
        print('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))
        p += 1

    num = int(x * (2 ** p))

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num // 2

    for i in range(p - len(result)):
        result = '0' + result

    result = result[0:-p] + '.' + result[-p:]
    print('Бинарное выражение числа с плавающей точкой: ' + str(x) + ' is ' + str(result))
