# Kids With the Greatest Candies (Дети c наибольшим количеством конфет)
# Нам дается массив целых чисел, который представляет количество конфет, полученных некоторыми детьми,
# и несколько дополнительных конфет, которые можно распределить любым способом.
# Задача: проверить, есть ли способ распределить дополнительные конфеты среди детей таким образом,
# чтобы каждому досталось наибольшее количество конфет среди них.
#
# candies = [2, 3, 5, 1, 3] # максимум конфет у третьего 5 шт.
# extra_candies = 3 # сколько даем каждому доп.конфет
# 2+3=5, 3+3=6, 5+3=8, 1+3=4, 3+3=6 # смотрим сколько будет в итоге после раздачи
# Output: [true, true, true, false, true] # если 5 и более то True

candies = [2, 3, 6, 1, 3]
extra_candies = 3


def kids_with_candies(candies, extra_candies):
    """Kids With the Greatest Candies"""
    return [candy + extra_candies >= max(candies) for candy in candies]


if __name__ == '__main__':
    print(kids_with_candies(candies, extra_candies))
