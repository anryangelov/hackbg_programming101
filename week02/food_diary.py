import datetime


filename = 'food_diary.txt'
message = '''\
Choose an option.
1. meal - to write what are you eating now.
2. list <dd.mm.yyyy> - lists all the meals that you ate that day,
'''


def add_food(food):
    today = datetime.date.today()
    today_str = "{}.{}.{}".format(today.day, today.month, today.year)
    with open(filename, 'a') as f:
        f.write("{}:{}\n".format(today_str, food))


def get_food(date):
    res = []
    with open(filename) as f:
        for row in f:
            row = row.strip()
            if row.startswith(date):
                res.append(row.split(':')[1])
    return res


def console():
    print("\nHello and Welcome!")
    print(message)
    while True:
        words = input("Enter command> ")
        words = words.split(None, 1)
        if not words:
            continue
        if len(words) < 2:
            print("Need more arguments")
            continue
        option, arg = words
        if option == 'meal':
            add_food(arg)
        elif option == 'list':
            food = get_food(arg)
            if not food:
                continue
            print('\n'.join(food))
        else:
            print("\nInvalid Option")
            print(message)


if __name__ == '__main__':
    console()
