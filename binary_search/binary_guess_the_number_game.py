def binary_guess_the_number_game():
    """
    Игра в угадайку!
    Программа работает следующим образом: вы (пользователь) думаете о целом числе от 0 (включительно)
    до 100 (не включительно). Компьютер делает предположение и вы даете ему входные данные - либо он поднимается
    слишком высоко, либо опускается слишком низко.
    Используя поиск по разделению пополам, компьютер угадает секретный номер пользователя
    """
    x = input('Please think of a number between 0 and 100! Enter a number: ')

    while not x.isdigit():
        print('Sorry, I did not understand your input.')
        x = input('Try again: ')
        if isinstance(x, int) > 100:
            print('Sorry, I did not understand your input.')
            x = input('Try again: ')

    epsilon = 1
    num_guesses = 0
    low = 0
    high = 100
    result = int((high + low) / 2)

    while abs(result - int(x)) >= 0:
        print('Is your secret number ' + str(result) + '?')
        ans = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                        "Enter 'c' to indicate I guessed correctly."))
        if ans == 'l':
            low = result
        elif ans == 'h':
            high = result
        elif ans == 'c':
            print('Game over. Your secret number was: ' + str(result))
            break
        else:
            print('Sorry, I did not understand your input.')
        result = int((high + low) / 2)


if __name__ == '__main__':
    binary_guess_the_number_game()
