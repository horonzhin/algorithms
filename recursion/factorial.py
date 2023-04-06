def simple_factorial(n):
    """Поиск факториала при помощи рекурсии"""
    # Для того чтобы рекурсия не ушла в бесконечный цикл, нужно задавать конечное условие.
    if n == 1:
        return 1
    return n * simple_factorial(n - 1)


if __name__ == '__main__':
    print(simple_factorial(3))
