import asyncio
from time import sleep, time
from faker import Faker

fake = Faker("uk-UA")


def get_user_from_db(uuid: int):
    sleep(0.5)
    return {"id": uuid, "name": fake.user_name(), "email": fake.email()}


async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "name": fake.user_name(), "email": fake.email()}


async def main():
    users = []
    for i in range(1, 6):
        users.append(async_get_user_from_db(i))
    result = await asyncio.gather(*users)
    return result


if __name__ == "__main__":
    start_time = time()
    for i in range(1, 6):
        print(get_user_from_db(i))
    print(time() - start_time)

    start_time = time()
    users = asyncio.run(main())
    [print(user) for user in users]
    print(time() - start_time)
