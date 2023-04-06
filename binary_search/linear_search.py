def linear_search(arr, target):
    """Метод поиска элементов в списке. Его еще называют последовательным поиском."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i


if __name__ == "__main__":
    arr = [2, 5, 8, 10, 16, 22, 25]
    target = 10
    print(linear_search(arr, target))
