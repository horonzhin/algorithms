def binary_search_symbol_recursion_slow(char, arr):
    """Бинарный поиск символа в строке с использованием рекурсии. Сложность O(n^2)"""
    if arr == "":
        return False
    elif len(arr) == 1 and arr == char:
        return True
    elif len(arr) == 1 and arr != char:
        return False
    elif arr[len(arr) // 2] == char:
        return True
    else:
        if char < arr[len(arr) // 2]:
            return binary_search_symbol_recursion_slow(char, arr[:len(arr) // 2])
        else:
            return binary_search_symbol_recursion_slow(char, arr[len(arr) // 2:])


def binary_search_symbol_recursion_fast(arr, char):
    """Бинарный поиск символа в строке с использованием рекурсии. Сложность O(n log n)"""
    def binary_search_helper(arr, char, low, high):
        if high == low:
            return arr[low] == char
        mid = (low + high) // 2
        if arr[mid] == char:
            return True
        elif arr[mid] > char:
            if low == mid:
                return False
            else:
                return binary_search_helper(arr, char, low, mid - 1)
        else:
            return binary_search_helper(arr, char, mid + 1, high)

    if len(arr) == 0:
        return False
    else:
        return binary_search_helper(arr, char, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = 'abcdefghijklmnopqrstuvwxyz'
    char = 'e'
    print(binary_search_symbol_recursion_slow(char, arr))
    print(binary_search_symbol_recursion_fast(arr, char))
