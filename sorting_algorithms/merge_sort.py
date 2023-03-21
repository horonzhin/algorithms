# Merge Sort (Сортировка слиянием)
#
# Делим список пополам на два равных (и так можно делить столько раз, сколько раз можно разделить уже
# разделенные списки) и отсортируем каждый. Затем берем берем первый элемент из каждого, сравниваем их и помещаем в
# результирующий список наименьший и т.д. Как только один из пары элементов будет пустым, просто копируем остаточную
# часть в результирующий список.
# Сложность O(n log n).

# Объединяем списки:

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        i += 1
    return result


# Делим и объединяем списки:

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)
