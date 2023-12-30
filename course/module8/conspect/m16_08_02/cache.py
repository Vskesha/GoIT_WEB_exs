import redis
from redis_lru import RedisLRU

client = redis.Redis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)


@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(f'Result fib(35): {fibonacci(35)}')
