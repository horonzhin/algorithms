# Hangman game

# Вариация классической словесной игры "Палач" - это игра в угадайку для двух или более игроков.
# Один игрок думает о слове, фразе или предложении, а другой пытается угадать его,
# предлагая буквы в пределах определенного количества догадок. В этой игре вторым игроком всегда будет компьютер,
# который будет выбирать слово наугад.

# -----------------------------------
# Helper code

import random
import string

alph = string.ascii_lowercase

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list


def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(word_list)


# end of helper code
# -----------------------------------

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed; False otherwise
    """
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    """
    result = []
    for i in secret_word:
        if i in letters_guessed:
            result.append(i)
        else:
            result.append("_")
    return " ".join(result)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not yet been guessed.
    """
    remain = []
    for i in alph:
        if i not in letters_guessed:
            remain.append(i)
    return ''.join(remain)
    

def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secret_word), "letters long.")
    mistakes_made = 0
    letters_guessed = []

    while mistakes_made < 8:
        if is_word_guessed(secret_word, letters_guessed):
            print('------------')
            print('Congratulations, you won!')
            break
        else:
            print('------------')
            print('You have', 8 - mistakes_made, 'guesses left.')
            print('Available letters:', get_available_letters(letters_guessed))
            guess = str(input('Please guess a letter:')).lower()
            if guess in secret_word and guess not in letters_guessed:
                letters_guessed.append(guess)
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            elif guess in letters_guessed:
                print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            elif guess not in secret_word:
                mistakes_made += 1
                letters_guessed.append(guess)
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        if mistakes_made == 8:
            print('------------')
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break
        else:
            continue


if __name__ == '__main__':
    secret_word = choose_word(wordlist).lower()
    hangman(secret_word)
