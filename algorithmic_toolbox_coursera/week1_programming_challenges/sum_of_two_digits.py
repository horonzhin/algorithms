def sum_of_digits(first_digit, second_digit):
    """Сумма двух чисел"""
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_digits(a, b))
