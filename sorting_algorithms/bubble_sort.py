# Bubble Sort (Пузырьковая сортировка)
# Cравниваем последовательные элементы. Меняем их местами так, чтобы меньший всегда был первым в этой паре.
# Смотрим на первые два элемента и если второй элемент будет меньше первого, производим замену.
# Затем смотрим на второй и третий, затем на третий и четвертый и т.д.
# Сложность O(n^2)

def bubble_sort_1(arr):
    """Bubble Sort (Пузырьковая сортировка)"""
    swap = False
    iterations = 0
    while not swap:
        swap = True
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                iterations += 1
                swap = False
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr, iterations


def bubble_sort_2(arr):
    """Bubble Sort (Пузырьковая сортировка)"""
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, iterations


if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort_1(arr))
    print(bubble_sort_2(arr))
