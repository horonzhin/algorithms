def square_root_calculations():
    """
    Метод Ньютон-Рафсон. Метод вычисления квадратного корня
    Простой и эффективный алгоритм для приближенного нахождения корня
    """
    epsilon = 0.01
    y = float(input('Введите число: '))
    guess = y / 2.0
    num_guesses = 0

    while abs(guess * guess - y) >= epsilon:
        num_guesses += 1
        guess = guess - (((guess ** 2) - y) / (2 * guess))

    print('Num guesses: ' + str(num_guesses))
    print('Квадратный корень из ' + str(y) + ' = ' + str(guess))


if __name__ == '__main__':
    square_root_calculations()
