# Selection Sort (Сортировка по выбору)
#
# Находим минимальный элемент (пройдясь по всему списку) и меняем его местами с элементом на 0 индексе.
# Далее проходим по всему списку находим минимальный и меняем его местами с элементом на 1 индексе и т.д.
# Сложность тоже O(n^2), но в сравнении с Bubble Sort, по времени Selection Sort чуть быстрее.

def selection_sort(arr):
    suffix_st = 0
    while suffix_st != len(arr):
        for i in range(suffix_st, len(arr)):
            if arr[i] < arr[suffix_st]:
                arr[suffix_st], arr[i] = arr[i], arr[suffix_st]
            suffix_st += 1
