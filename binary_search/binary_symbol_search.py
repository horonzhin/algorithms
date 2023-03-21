# Бинарный поиск символа в строке с использованием рекурсии. Сложность O(n^2):

def is_in(char, string):
    if string == "":
        return False
    elif len(string) == 1 and string == char:
        return True
    elif len(string) == 1 and string != char:
        return False
    elif string[len(string) // 2] == char:
        return True
    else:
        if char < string[len(string) // 2]:
            return is_in(char, string[:len(string) // 2])
        else:
            return is_in(char, string[len(string) // 2:])


# Бинарный поиск символа в строке с использованием рекурсии. Сложность O(n log n):

def bisect_search(arr, char):
    def bisect_search_helper(arr, char, low, high):
        if high == low:
            return arr[low] == char
        mid = (low + high) // 2
        if arr[mid] == char:
            return True
        elif arr[mid] > char:
            if low == mid:
                return False
            else:
                return bisect_search_helper(arr, char, low, mid - 1)
        else:
            return bisect_search_helper(arr, char, mid + 1, high)

    if len(arr) == 0:
        return False
    else:
        return bisect_search_helper(arr, char, 0, len(arr) - 1)
