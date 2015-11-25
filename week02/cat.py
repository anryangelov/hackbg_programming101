'''cat.py'''


import sys


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print("need to enter filename")
        quit()
    with open(filename) as f:
        cont = f.read()
    print(cont)


if __name__ == '__main__':
    main()
