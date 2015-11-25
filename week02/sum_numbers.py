import sys


def main():
    res = 0
    try:
        filename = sys.argv[1]
    except IndexError:
        print("need to enter filename")
        quit()
    with open(filename) as f:
        for line in f:
            line = line.strip()
            for digit in line.split(" "):
                if digit.isdigit():
                    res += int(digit)
    return res


if __name__ == '__main__':
    print(main())
