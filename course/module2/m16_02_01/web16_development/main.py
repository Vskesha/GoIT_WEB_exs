from typing import TypedDict, Literal, NamedTuple
from dataclasses import dataclass


class UserInfo(TypedDict):
    id: int
    username: str
    email: str
    is_active: bool


@dataclass(frozen=True)
class UserSchema:
    id: int
    username: str
    email: str
    is_active: bool = True


class Cat(NamedTuple):
    nick: str
    age: int


User = {
    'id': 23,
    'username': 'Dmytro',
    'email': 'dmytro@example.com',
    'is_active': True
}


def get_user() -> UserInfo:
    return User


def get_user_info() -> UserSchema:
    return UserSchema(id=23, username='Dmytro', email='dmytro@example.com')


def mul(data: list) -> float:
    result = 1
    for num in data:
        result *= num
    return result


Shape = Literal['circle', 'square']


def foo(shape: Shape):
    if shape == 'circle':
        print('It is a circle')
    elif shape == 'square':
        print('It is a square')


if __name__ == '__main__':
    print(mul([2]))
    print(get_user()['username'])
    foo('circle')
    cat = Cat(nick='Simon', age=5)
    print(cat.nick)