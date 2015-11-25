# generate_numbers.py
import sys
from random import randint


def main():
    try:
        filename = sys.argv[1]
        n = sys.argv[2]
    except IndexError:
        print("need arguments filename and integer")
        quit()
    cont = []
    for i in range(int(n)):
        number = str(randint(1, 1000))
        cont.append(number)
    with open(filename, 'w') as f:
        f.write(" ".join(cont))


if __name__ == '__main__':
    main()
