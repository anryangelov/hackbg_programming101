def sum_of_digit1(n):
    if n < 0:
        n = n * -1
    res = 0
    for digit in str(n):
        res += int(digit)
    return res


def sum_of_digit(n):
    if n < 0:
        n = n * -1
    res = 0
    while n > 10:
        res += n % 10
        n = n // 10
    return res + n


print(sum_of_digit(1325132435356))
print(sum_of_digit(123))
print(sum_of_digit(6))
print(sum_of_digit(-10))
print()


def to_digits(n):
    res = []
    while n > 10:
        res.insert(0, (n % 10))
        n = n // 10
    res.insert(0, n)
    return res

print(to_digits(123))
print(to_digits(99999))
print(to_digits(123023))
print()


def to_number(digits):
    res = 0
    l = len(digits) - 1
    for digit in digits:
        res += digit * (10**l)
        l -= 1
    return res


print(to_number([1, 2, 3]))
print(to_number([9, 9, 9, 9, 9]))
print(to_number([1, 2, 3, 0, 2, 3]))
print()


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


print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))
print()


def fibonacci(n):
    res = []
    a = 1
    b = 1
    while n > 0:
        res.append(a)
        a, b = b, a + b
        n -= 1
    return res


print(fibonacci(3))
print(fibonacci(10))
print()


def fib_numbers(n):
    digits = []
    for number in fibonacci(n):
        if number > 9:
            for digit in to_digits(number):
                digits.append(digit)
        else:
            digits.append(number)
    return to_number(digits)


print(fib_numbers(3))
print(fib_numbers(10))
print()


def palindrome(n):
    n = str(n)
    return n == ''.join(reversed(n))


print(palindrome(121))
print(palindrome("kapak"))
print(palindrome("baba"))
print()


def count_vowels(s):
    count = 0
    for letter in s.lower():
        if letter in "aeiouy":
            count += 1
    return count


print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("grrrrgh!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_vowels("A nice day to code!"))
print()


def count_consonants(s):
    count = 0
    for letter in s.lower():
        if letter in "bcdfghjklmnpqrstvwxz":
            count += 1
    return count


print(count_consonants("Python"))
print(count_consonants("Theistareykjarbunga"))
print(count_consonants("grrrrgh!"))
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_consonants("A nice day to code!"))
print()


def char_histogram(s):
    res = {}
    for letter in s:
        res[letter] = res.get(letter, 0) + 1
    return res


print(char_histogram("Python!"))
print(char_histogram("AAAAaaa!!!"))




