'''
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1

>>> to_digits(123)
[1, 2, 3]
>>> to_digits(99999)
[9, 9, 9, 9, 9]
>>> to_digits(123023)
[1, 2, 3, 0, 2, 3]

>>> to_number([1,2,3])
123
>>> to_number([9,9,9,9,9])
99999
>>> to_number([1,2,3,0,2,3])
123023
>>> to_number([21, 2, 33])
21233

>>> fact_digits(111)
3
>>> fact_digits(145)
145
>>> fact_digits(999)
1088640

>>> fibonacci(1)
[1]
>>> fibonacci(2)
[1, 1]
>>> fibonacci(3)
[1, 1, 2]
>>> fibonacci(10)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

>>> fib_number(3)
112
>>> fib_number(10)
11235813213455

>>> palindrome(121)
True
>>> palindrome("kapak")
True
>>> palindrome("baba")
False

>>> count_vowels("Python")
2
>>> count_vowels("Theistareykjarbunga") #It's a volcano name!
8
>>> count_vowels("grrrrgh!")
0
>>> count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
22
>>> count_vowels("A nice day to code!")
8

>>> count_consonants("Python")
4
>>> count_consonants("Theistareykjarbunga") #It's a volcano name!
11
>>> count_consonants("grrrrgh!")
7
>>> count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
44
>>> count_consonants("A nice day to code!")
6

>> char_histogram("Python!") == { 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 }
True
>>> char_histogram("AAAAaaa!!!") == { 'A': 4, 'a': 3, '!': 3 }
True
'''


def sum_of_digits(n):
    if n < 0:
        n = n * -1
    res = 0
    while n > 9:
        res += n % 10
        n = n // 10
    return res + n


def to_digits(n):
    res = []
    while n > 10:
        res.insert(0, (n % 10))
        n = n // 10
    res.insert(0, n)
    return res


def to_number(digits):
    res = 0
    small_digits = []
    for number in digits:
        if number > 9:
            for digit in to_digits(number):
                small_digits.append(digit)
        else:
            small_digits.append(number)
    l = len(small_digits) - 1
    for digit in small_digits:
        res += digit * (10**l)
        l -= 1
    return res


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def fact_digits(n):
    res = 0
    for digit in to_digits(n):
        f = factorial(digit)
        res += f
    return res


def fibonacci(n):
    res = []
    a = 1
    b = 1
    while n > 0:
        res.append(a)
        a, b = b, a + b
        n -= 1
    return res


def fib_number(n):
    digits = []
    for number in fibonacci(n):
        if number > 9:
            for digit in to_digits(number):
                digits.append(digit)
        else:
            digits.append(number)
    return to_number(digits)


def palindrome(n):
    n = str(n)
    return n == ''.join(reversed(n))


def count_vowels(s):
    count = 0
    for letter in s.lower():
        if letter in "aeiouy":
            count += 1
    return count


def count_consonants(s):
    count = 0
    for letter in s.lower():
        if letter in "bcdfghjklmnpqrstvwxz":
            count += 1
    return count


def char_histogram(s):
    res = {}
    for letter in s:
        res[letter] = res.get(letter, 0) + 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
