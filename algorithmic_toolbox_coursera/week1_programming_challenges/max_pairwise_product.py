def max_pairwise_product(numbers):
    """Поиск максимального произведения двух чисел из последовательности положительных чисел. Сложность O(n^2)"""
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    """Поиск максимального произведения двух чисел из последовательности положительных чисел. Сложность O(n log n)"""
    if len(numbers) == 1:
        return numbers[0]
    numbers = sorted(numbers, reverse=True)
    result = numbers[0] * numbers[1]
    return result


if __name__ == '__main__':
    amount_of_numbers = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast(input_numbers))
