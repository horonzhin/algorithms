def fibonacci_last_digit(n):
    """
    Вычисление Фибоначчи с использованием временных переменных и итерации.
    В данном случае сложность O(n), но если числа будут очень большими, то сложность может увеличиться до O(n^2).
    """
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


if __name__ == '__main__':
    input_n = int(input('Введите число для вычисления Фибоначчи: '))
    print(f'Фибоначчи числа {input_n} с помощью итерации: {fibonacci_last_digit(input_n)}')
