import random


class Hand(object):
    def __init__(self, n):
        """
        Initialize a Hand.

        n: integer, the size of the hand.
        """
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.deal_new_hand()

    def deal_new_hand(self):
        """
        Deals a new hand, and sets the hand attribute to the new hand.
        """
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        num_vowels = self.HAND_SIZE // 3
    
        for i in range(num_vowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(num_vowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def set_dummy_hand(self, hand_string):
        """
        Allows you to set a dummy hand. Useful for testing your implementation.

        hand_string: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        """
        assert len(hand_string) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})"\
            .format(len(hand_string), self.HAND_SIZE)
        self.hand = {}
        for char in hand_string:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculate_len(self):
        """
        Calculate the length of the hand.
        """
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        """
        Display a string representation of the hand.
        """
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume this self.hand has all the letters in word.

        Updates the distribution: if self.hand has all the letters that need to be composed
        the word, modifies self.hand, using the letters in the given word.

        Returns True if the word was formed using the letter b
        hand; otherwise false.

        word: string
        returns: Boolean value (if the word was or was not created)
        """
        word_letter_list = list(word)
        hand_letter_list = []

        for i in self.hand.keys():
            for j in range(self.hand[i]):
                hand_letter_list.append(i)

        def is_valid_word(word):
            """
            Returns True if word is entirely composed of letters in the hand.
            Otherwise, returns False.
            Does not mutate hand or wordList.

            word: string
            hand: dictionary (string -> int)
            wordList: list of lowercase strings
            """
            output = self.hand.copy()
            letter_check = set(list(word)) <= set(output.keys())
            for letter in word:
                if letter in output.keys():
                    output[letter] -= 1

            value_check = all(i >= 0 for i in output.values())
            if letter_check == True and value_check == True:
                return True
            else:
                return False

        if is_valid_word(word):
            output = self.hand.copy()
            for letter in word_letter_list:
                if letter in output.keys():
                    output[letter] -= 1
            self.hand = {k: output[k] for k in output if output[k] != 0}
            return True
        else:
            return False


if __name__ == '__main__':

    my_hand = Hand(7)
    print(my_hand)
    print(my_hand.calculate_len())

    my_hand.set_dummy_hand('aazzmsp')
    print(my_hand)
    print(my_hand.calculate_len())

    my_hand.update('za')
    print(my_hand)
