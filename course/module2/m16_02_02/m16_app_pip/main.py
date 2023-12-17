import sys


def print_hi(name):
    try:
        print(sys.argv[1])
    except IndexError:
        print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
