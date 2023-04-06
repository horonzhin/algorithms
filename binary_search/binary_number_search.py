def binary_search_number_iteration(arr, start, end, target):
    """Бинарный поиск индекса числа в массиве с использованием итерации"""
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return start


def binary_search_number_recursion(arr, start, end, target):
    """Бинарный поиск индекса числа в массиве с использованием рекурсии"""
    if end >= start:
        mid = start + end - 1 // 2
        if arr[mid] < target:
            binary_search_number_recursion(arr, mid + 1, end, target)
        elif arr[mid] > target:
            return binary_search_number_recursion(arr, start, mid - 1, target)
        else:
            return mid
    else:
        return -1


if __name__ == '__main__':
    arr = [2, 5, 8, 10, 16, 22, 25]
    target = 10
    print(f'Использование итерации: {binary_search_number_iteration(arr, 0, len(arr) - 1, target)}')
    print(f'Использование рекурсии: {binary_search_number_recursion(arr, 0, len(arr) - 1, target)}')
