import random


def get_output():
    return 'Hello, world!\nAndhiagain!\n' + '!' * random.randint(5, 50)


def task1():
    print(get_output())


if __name__ == '__main__':
    task1()
