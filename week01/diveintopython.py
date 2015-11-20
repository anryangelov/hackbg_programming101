'''
>>> is_number_balanced(9)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True

>>> is_increasing([1,2,3,4,5])
True
>>> is_increasing([1])
True
>>> is_increasing([5,6,-10])
False
>>> is_increasing([1,1,1,1])
False

>>> is_decreasing([5,4,3,2,1])
True
>>> is_decreasing([1,2,3])
False
>>> is_decreasing([100, 50, 20])
True
>>> is_decreasing([1,1,1,1])
False

>>> get_largest_palindrome(99)
88
>>> get_largest_palindrome(252)
242
>>> get_largest_palindrome(994687)
994499
>>> get_largest_palindrome(754649)
754457

>>> prime_numbers(30)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> prime_numbers(3)
[2, 3]

>>> is_anagram("BRADE", "BeaRD")
True
>>> is_anagram("TOP_CODER", "COTO_PRODE")
False

>>> birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
[2, 3, 4, 5, 2]

>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum_matrix(m)
45
>>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> sum_matrix(m)
0
>>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> sum_matrix(m)
55

>>> from pprint import pprint
>>> pprint(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}

>>> is_transversal((4, 5, 6), ((5, 7, 9), (1, 4, 3), (2, 6)))
True
>>> is_transversal((1, 2), ((1, 5), (2, 3), (4, 7)))
False
>>> is_transversal((2, 3, 4), ((1, 7), (2, 3, 5), (4, 8)))
False

>>> generate_transversals([[1, 4, 5], [2, 7], [1, 9]])
[[1, 2], [1, 7], [2, 4, 9], [2, 5, 9], [4, 7, 9], [5, 7, 9]]
>>> generate_transversals([[7,8], [2, 3, 4]])
[[8, 2], [8, 3], [8, 4], [2, 7], [3, 7], [4, 7]]
'''

from firstday import palindrome, char_histogram
from itertools import combinations


def is_number_balanced(n):
    s = str(n)
    if len(s) == 1:
        return True
    left, right = 0, 0
    midle = len(s) // 2
    end = len(s) - 1
    for i in range(midle):
        left += int(s[i])
        right += int(s[end - i])
    return left == right


def is_increasing(seq):
    previous = seq[0] - 1
    for integer in seq:
        if not integer > previous:
            return False
        previous = integer
    return True


def is_decreasing(seq):
    previous = seq[0] + 1
    for integer in seq:
        if not integer < previous:
            return False
        previous = integer
    return True


def get_largest_palindrome(n):
    r = reversed(range(n))
    for number in r:
        if palindrome(number):
            return number


def prime_numbers(n):
    l = list(range(2, n + 1))
    for number in l:
        for index, n in enumerate(l):
            if n == number:
                continue
            if (n % number) == 0:
                l.pop(index)
    return [2] + l[1:]


def is_anagram(a, b):
    return char_histogram(a.lower()) == char_histogram(b.lower())


def birthday_ranges(birthdays, ranges):
    res = []
    for r in ranges:
        count = 0
        for birthday in birthdays:
            if r[0] <= birthday <= r[1]:
                count += 1
        res.append(count)
    return res


def sum_matrix(m):
    res = 0
    for row in m:
        res += sum(row)
    return res


def get_neighbours_indexes(a, b, row_limit, column_limit):
    res = []
    for i in (a - 1, a, a + 1):
        for j in (b - 1, b, b + 1):
            if row_limit > i >= 0 and column_limit > j >= 0 and (i, j) != (a, b):
                res.append((i, j))
    return res


def matrix_bombing_plan(m):
    res = {}
    max_rows = len(m)
    max_columns = len(m[0])
    for row in range(max_rows):
        for column in range(max_columns):
            bomb_value = m[row][column]
            copy_m = [m[i].copy() for i in range(max_rows)] # deep copy
            for i, j in get_neighbours_indexes(row, column, max_rows, max_columns):
                copy_m[i][j] -= bomb_value
                if copy_m[i][j] < 0:
                    copy_m[i][j] = 0
            damage = sum_matrix(copy_m)
            res[(row, column)] = damage
    return res


def is_transversal(transversal, family):
    for s in family:
        if set(transversal).isdisjoint(set(s)):
            return False
    return True


def issubset(lists, check_list):
    for one_list in lists:
        if set(one_list).issubset(set(check_list)):
            return False
    return True


def generate_transversals(family):
    res = []
    elements = set()
    for s in family:
        elements.update(s)
    for i in range(1, len(elements)):
        for comb in combinations(elements, i):
            if is_transversal(comb, family):
                if issubset(res, comb):
                    res.append(list(comb))
    return res

print(generate_transversals([[7,8], [2, 3, 4]]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
