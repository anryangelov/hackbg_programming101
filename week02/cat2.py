'''cat2.py'''


import sys


def main():
    cont = ''
    filenames = sys.argv[1:]
    if len(filenames) == 0:
        print("need to enter filename")
        quit()
    for filename in filenames:
        with open(filename) as f:
            cont += f.read()
    print(cont, end='')


if __name__ == '__main__':
    main()
