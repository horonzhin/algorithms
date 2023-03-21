# Последовательность Фибоначчи с помощью рекурсии

def fibo_1(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibo_1(x - 1) + fibo_1(x - 2)


# Вычисление Фибоначчи с использованием словаря, более эффективное вычисление чем при обычной рекурсии

def fibo_2(n, temp_dict):
    if n in temp_dict:
        return temp_dict[n]
    else:
        ans = fibo_2(n - 1, temp_dict) + fibo_2(n - 2, temp_dict)
        temp_dict[n] = ans
        return ans


n = 100
temp_dict = {1: 1, 2: 2}
print(fibo_2(n, temp_dict))

