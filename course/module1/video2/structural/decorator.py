class Greeting:
    def __init__(self, username):
        self.username = username

    def greet(self):
        return f'Hello, {self.username}!'


class GreetingDecorator:
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def greet(self):
        res = self.wrapper.greet()
        return res.upper()


if __name__ == '__main__':
    user = GreetingDecorator(Greeting('Oleh'))
    print(user.greet())
