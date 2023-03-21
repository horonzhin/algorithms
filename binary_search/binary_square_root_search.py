# Бинарный поиск квадратного корня из X:

x = int(input('Введите целое число: '))
epsilon = 0.01
num_guesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= epsilon:
    print('low =' + str(low) + 'high =' + str(high) + 'ans =' + str(ans))
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

if __name__ == '__main__':
    print('num_guesses = ' + str(num_guesses))
    print(str(ans) + ' is close to square root of ' + str(x))
