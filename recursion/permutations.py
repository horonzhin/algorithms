from math import factorial


# Алгоритм перестановок (permutations)
# Поиск всевозможных вариаций с определенным набором элементов.
# ABC имеет 6 возможных вариаций ABC * ACB * BAC * BCA * CAB * CBA. Это факториал 3.
# Удаляем первый элемент и создаем 2 подмножества элементов, которые меняются местами, а затем возвращается удаленный.
# ABC -> удаляем А меняем BC на СВ возвращаем А -> ACB
# ABC -> удаляем следующий элемент B меняем AC на CA возвращаем B -> BAC и BCA
# ABC -> удаляем следующий элемент C меняем AB на BA возвращаем C -> CAB и CBA

def permutations_recursion(string, pocket=''):
    """Алгоритм перестановок (permutations) на основе рекурсии"""
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i + 1:]
            together = front + back
            permutations_recursion(together, letter + pocket)


def permutations_iteration(string):
    """
    Алгоритм перестановок (permutations) на основе итерации
    Более оптимизированный по сравнению с использованием рекурсии
    """
    for p in range(factorial(len(string))):
        print(''.join(string))
        i = len(string) - 1
        while i > 0 and string[i - 1] > string[i]:
            i -= 1
        string[i:] = reversed(string[i:])
        if i > 0:
            q = i
            while string[i - 1] > string[q]:
                q += 1
            temp = string[i - 1]
            string[i - 1] = string[q]
            string[q] = temp


# 8/n Queens Problem
# Задача в том, чтобы разместить 8 ферзей на шахматной доке 8*8 так, чтобы никто не мог атаковать никого.
# Есть 4 000 000 000 варианта расстановок 8 ферзей на доске и всего 92 решения этой проблемы.
# Это очень дорогостоящее решение в плане вычислительной мощности.
# Использование перестановок (permutations) может сократить с 4 миллиардов до 40 000 вариантов расстановок.

if __name__ == '__main__':
    s = 'ABC'
    s = list(s)
    permutations_recursion('ABC', '')  # permutations_recursion('ABC') - выполнится за 156 шагов
    print('************************')
    permutations_iteration(s)  # permutations_iteration(s) - выполнится за 79 шагов
