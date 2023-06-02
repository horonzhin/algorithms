def fibo_recursion(x):
    """Последовательность Фибоначчи с помощью рекурсии. Сложность O(2^n)"""
    if x <= 1:
        return x
    else:
        return fibo_recursion(x - 1) + fibo_recursion(x - 2)


def fibo_dict(n, temp_dict):
    """
    Вычисление Фибоначчи с использованием словаря.
    Более эффективное вычисление чем при обычной рекурсии.
    В данном случае сложность O(n), но если числа будут очень большими, то сложность может увеличиться до O(n^2).
    """
    if n in temp_dict:
        return temp_dict[n]
    else:
        ans = fibo_dict(n - 1, temp_dict) + fibo_dict(n - 2, temp_dict)
        temp_dict[n] = ans
        return ans


def fibo_iteration(n):
    """"
    Вычисление Фибоначчи с использованием массива и итерации
    В данном случае сложность O(n), но если числа будут очень большими, то сложность может увеличиться до O(n^2).
    """
    arr = [0 for i in range(0, n + 1)]
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[-1]


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
    n = 20
    temp_dict = {0: 0, 1: 1, 2: 1}
    print(f'Фибоначчи числа {n} с помощью рекурсии: {fibo_recursion(n)}')
    print(f'Фибоначчи числа {n} с помощью словаря: {fibo_dict(n, temp_dict)}')
    print(f'Фибоначчи числа {n} с помощью массива и итерации: {fibo_iteration(n)}')
    print(f'Фибоначчи числа {n} с помощью переменных и итерации: {fibonacci_last_digit(n)}')
