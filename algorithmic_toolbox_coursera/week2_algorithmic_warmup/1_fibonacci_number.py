def fibonacci_number(n):
    """Последовательность Фибоначчи с помощью рекурсии. Сложность O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


if __name__ == '__main__':
    input_n = int(input('Введите число для вычисления Фибоначчи: '))
    print(f'Фибоначчи числа {input_n} с помощью рекурсии: {fibonacci_number(input_n)}')
