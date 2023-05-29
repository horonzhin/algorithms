import random
from week1_programming_challenges.max_pairwise_product import max_pairwise_product, max_pairwise_product_fast


def stress_test(max_amount, max_number):
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


if __name__ == "__main__":
    stress_test(1000, 100000)
