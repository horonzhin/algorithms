import functools
import random
import time
from algorithmic_toolbox_coursera.week1_programming_challenges.max_pairwise_product \
    import max_pairwise_product, max_pairwise_product_fast


def stress_test(max_amount, max_number):
    """
    Стресс-тест для поиска ошибок в алгоритме.
    Сравниваем две функции:
    Первая - грубая сила, не оптимизированный алгоритм, но рабочий.
    Вторая - оптимизированный алгоритм.
    """
    while True:
        amount = random.randint(2, max_amount)
        arr = []
        for i in range(amount):
            number = random.randint(0, max_number)
            arr.append(number)
        print(arr)
        result_1 = max_pairwise_product(arr)
        result_2 = max_pairwise_product_fast(arr)
        if result_1 == result_2:
            print("OK")
        else:
            print("Wrong answer", result_1, result_2)
            break


def timer(func):
    """Выводит время, затраченное на выполнение функции"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Выполнение функции заняло: {run_time:.4f} секунд".format(run_time=run_time))
        return value
    return wrapper


def calls_counter(func):
    """Подсчитывает количество вызовов функции"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls_count += 1
        value = func(*args, **kwargs)
        print(f"Количество вызовов функции: {wrapper.calls_count}")
        return value
    wrapper.calls_count = 0
    return wrapper


if __name__ == "__main__":
    stress_test(1000, 100000)
