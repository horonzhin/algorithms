def palindrome(s):
    """
    Поиск слов палиндромов с помощью рекурсии
    (число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях)
    """
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def is_palindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_palindrome(to_chars(s))


if __name__ == "__main__":
    s = 'tenet'
    print(palindrome(s))
