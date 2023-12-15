from typing import TypeVar, Iterable, Sequence

Number = int | float

T = TypeVar('T', int, str, float, list)


def calc(x: Number, y: Number) -> Number:
    return x + y


def calculator(x: T, y: T) -> T:
    return x + y


def total_length(items: Iterable[str]) -> int:
    return sum(len(item) for item in items)


def total_length_other(items: Sequence[str]) -> int:
    return sum(len(item) for item in items)


if __name__ == '__main__':
    print(calculator(3, 5))
    print(calculator('Hello ', 'World!'))
    print(calculator(3.5, 1.4))
    print(calculator([1, 2], [3, 4]))

    print(calc(3, 1.4))
    print(calculator(3, 1.4))

    print(total_length(('Maksym', 'Volodymyr', 'Artem')))
    print(total_length(['Maksym', 'Volodymyr', 'Artem']))
    print(total_length({'Maksym', 'Volodymyr', 'Artem'}))

    print(total_length_other(('Maksym', 'Volodymyr', 'Artem')))
    print(total_length_other(['Maksym', 'Volodymyr', 'Artem']))
    print(total_length_other({'Maksym', 'Volodymyr', 'Artem'}))
