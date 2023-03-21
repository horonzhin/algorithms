# Напишите программу, которая печатает самую длинную подстроку s, в которой буквы расположены в алфавитном порядке.

s = 'azcbobobegghakl'
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print("Самая длинная подстрока в алфавитном порядке:", longest)


# *********************************************************************************************************************
# Дается перемешанный список с одним удаленным элементом. Задача: найти этот элемент

def find_one(arr: list) -> int:
    res_arr = len(arr) + 1
    summary = res_arr * (res_arr + 1) / 2
    return int(summary) - sum(arr)


arr = [3, 5, 4, 1]
print(find_one(arr))


# *********************************************************************************************************************
# Дается перемешанный список с двумя удаленными элементами. Задача: найти эти элементы

def find_two(arr: list) -> tuple:
    dig1 = dig2 = 0
    arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i + 1] - arr[i] > 1:  # !!!!! OUT OF RANGE !!!!!
            if dig1:
                dig2 = i + 1
            else:
                dig1 = i + 1
    if dig1 == 0:
        dig2 = len(arr) + 2
        dig1 = len(arr) + 1
    if dig2 == 0:
        dig2 = len(arr) + 2
    return dig1, dig2


arr = [1, 3, 5]
print(find_two(arr))


# *********************************************************************************************************************
# Задача: поменять местами элементы в списке в обратном порядке, если есть вложенные списки их тоже поменять.
# Пример, если L = [[1, 2], [3, 4], [5, 6, 7]] тогда deep_reverse(L) преобразует список в [[7, 6, 5], [4, 3], [2, 1]]

def deep_reverse(arr):
    """
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    result = []
    for i in arr:
        result.append(i[::-1])
    arr[:] = result[::-1]
    return arr


# *********************************************************************************************************************

