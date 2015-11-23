'''
>>> count_words(["apple", "banana", "apple", "pie"]) == {'apple': 2, 'pie': 1, 'banana': 1}
True
>>> count_words(["python", "python", "python", "ruby"]) == {'ruby': 1, 'python': 3}
True

>>> nan_expand(0)
''
>>> nan_expand(1)
'Not a NaN'
>>> nan_expand(2)
'Not a Not a NaN'
>>> nan_expand(3)
'Not a Not a Not a NaN'

>>> iterations_of_nan_expand("")
0
>>> iterations_of_nan_expand("Not a NaN")
1
>>> iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
10
>>> iterations_of_nan_expand("Show these people!")
False

>>> group([1, 1, 1, 2, 3, 1, 1])
[[1, 1, 1], [2], [3], [1, 1]]
>>> group([1, 2, 1, 2, 3, 3])
[[1], [2], [1], [2], [3, 3]]

>>> max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])
4
>>> max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
3

>>> gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
[80, 140, 220, 290]
>>> gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
[70, 140, 210, 280, 350]

>>> sum_of_numbers("ab125cd3")
128
>>> sum_of_numbers("ab12")
12
>>> sum_of_numbers("ab")
0

>>> numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
'abc'
>>> numbers_to_message([2, 2, 2, 2])
'a'
>>> numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
'Ivo e Panda'

>>> message_to_numbers("abc")
[2, -1, 2, 2, -1, 2, 2, 2]
>>> message_to_numbers("a")
[2]
>>> message_to_numbers("Ivo e Panda")
[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
>>> message_to_numbers("aabbcc")
[2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]


'''


def count_words(arr):
    res = {}
    for word in arr:
        res[word] = res.get(word, 0) + 1
    return res


def nan_expand(times):
    if times == 0:
        return ''
    return ' '.join(["Not a"] * times) + " NaN"


# one more solution
def nan_expand_recur(times):
    if times == 0:
        return ''
    times -= 1
    return nan_expand_recur(times) + "Not a "


def nan_expand_2(times):
    if times == 0:
        return ''
    return nan_expand_recur(times) + 'NaN'


def iterations_of_nan_expand(expanded):
    if expanded == "":
        return 0
    if not expanded.endswith("NaN"):
        return False
    len_exp = len(expanded) - 3
    i1 = 0
    i2 = 6
    while (len_exp > i2):
        if not expanded[i1:i2] == "Not a ":
            return False
        i1 += 6
        i2 += 6
    if not i2 == len_exp:
        return False
    return i2 / 6


def group(l):
    res = []
    temp = l[0]
    temp_list = []
    for v in l:
        if not v == temp:
            res.append(temp_list)
            temp_list = []
        temp_list.append(v)
        temp = v
    res.append(temp_list)
    return res


def max_consecutive(items):
    curr_max = 0
    seq = group(items)
    for l in seq:
        if len(l) > curr_max:
            curr_max = len(l)
    return curr_max


def gas_stations(distance, tank_size, stations):
    res = []
    curr_tank_size = tank_size
    last_station = 0
    for station in stations + [distance]:
        station_dist = station - last_station
        if station_dist < curr_tank_size:
            curr_tank_size -= station_dist
        else:
            res.append(last_station)
            curr_tank_size = tank_size - station_dist
        last_station = station
    return res


def sum_of_numbers(st):
    temp = ""
    numbers = []
    for ch in st:
        if ch in "1234567890":
            temp += ch
        else:
            if not temp == "":
                numbers.append(int(temp))
                temp = ""
    if not temp == "":
        numbers.append(int(temp))
    return sum(numbers)


keypad = ((2, 'abc'), (3, 'def'), (4, 'ghi'), (5, 'jkl'),
    (6, 'mno'), (7, 'pqrs'), (8, 'tuv'), (9, 'wxyz'))


def fix_len(seq):
    res = []
    for l in seq:
        if 7 in l or 9 in l:
            max_len = 4
        else:
            max_len = 3
        while len(l) > max_len:
            l = l[:-max_len]
        res.append(l)
    return res


def numbers_to_message(seq):
    res = []

    mapper = {}
    for k, v in keypad:
        for i, letter in enumerate(v, 1):
            mapper[tuple([k] * i)] = letter

    grouped = group(seq)
    grouped = fix_len(grouped)
    capitalized = False
    for one_group in grouped:
        if 0 in one_group:
            res.append(' ' * len(one_group))
        elif 1 in one_group:
            capitalized = True
        elif -1 in one_group:
            continue
        else:
            letter = mapper[tuple(one_group)]
            if capitalized is True:
                letter = letter.upper()
                capitalized = False
            res.append(letter)

    return ''.join(res)


def message_to_numbers(message):
    res = []

    mapper = {}
    for digit, st in keypad:
        for i, char in enumerate(st, 1):
            mapper[char] = [digit] * i

    last_digit = None
    for char in message:
        if char == ' ':
            res.append(0)
            continue
        if char.isupper():
            res.append(1)
            char = char.lower()
        digits = mapper.get(char, None)
        if digits:
            if digits[0] == last_digit:
                res.append(-1)
            res += digits
            last_digit = digits[0]
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
