import asyncio
from time import time, sleep

fake_users = [
    {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'},
    {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'},
    {'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
]


def get_user_sync(uid: int) -> dict:
    sleep(1)
    user, = list(filter(lambda u: u['id'] == uid, fake_users))
    return user


def sync_main():
    start = time()
    for i in range(1, 4):
        print(get_user_sync(i))
    print(f'Sync take {time() - start} seconds')


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(1)
    user, = list(filter(lambda u: u['id'] == uid, fake_users))
    return user


async def async_main():
    r = []
    for i in range(1, 4):
        r.append(get_user_async(i))
    return await asyncio.gather(*r)

if __name__ == '__main__':
    sync_main()
    start = time()
    result = asyncio.run(async_main())
    for r in result:
        print(r)
    print(f'Async take {time() - start} seconds')