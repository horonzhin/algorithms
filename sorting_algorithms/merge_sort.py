# Merge Sort (Сортировка слиянием)
# Делим список пополам на два равных (и так можно делить столько раз, сколько раз можно разделить уже
# разделенные списки) и отсортируем каждый. Затем берем первый элемент из каждого, сравниваем их и помещаем в
# результирующий список наименьший и т.д. Как только один из пары элементов будет пустым, просто копируем остаточную
# часть в результирующий список.
# Сложность O(n log n)

def merge_sort_bad_solution(unsorted_array):
    """Merge Sort с использованием грубой силы. Сложность O(n^2)"""
    result_array = []
    while unsorted_array:
        minimum = unsorted_array[0]
        for x in unsorted_array:
            if x < minimum:
                minimum = x
        result_array.append(minimum)
        unsorted_array.remove(minimum)
    return result_array


def merge_sort_recursion(unsorted_array):
    """Merge Sort с использованием рекурсии. Метод сверху вниз. Сложность O(n log n)"""
    if len(unsorted_array) <= 1:
        return unsorted_array
    middle = len(unsorted_array) // 2
    left = merge_sort_recursion(unsorted_array[:middle])
    right = merge_sort_recursion(unsorted_array[middle:])
    result_array = []
    while left and right:
        if left[0] <= right[0]:
            result_array.append(left.pop(0))
        else:
            result_array.append(right.pop(0))
    result_array.extend(right if right else left)
    return result_array


def merge_sort_iteration(unsorted_array):
    """Merge Sort при помощи итерации и встроенной функции sorted(). Метод снизу вверх. Сложность O(n log n)"""
    if len(unsorted_array) <= 1:
        return unsorted_array
    middle = len(unsorted_array) // 2
    left = sorted(unsorted_array[:middle])
    right = sorted(unsorted_array[middle:])
    result_array = []
    while left and right:
        if left[0] <= right[0]:
            result_array.append(left.pop(0))
        else:
            result_array.append(right.pop(0))
    result_array.extend(right if right else left)
    return result_array


if __name__ == '__main__':
    unsorted_array = [-5, -23, 5, 0, 23, -6, 23, 67]
    # print(merge_sort_bad_solution(unsorted_array))  # ~160 итераций для 10 элементов
    # print(merge_sort_recursion(unsorted_array))
    print(merge_sort_iteration(unsorted_array))  # 34 итерации для 10 элементов

