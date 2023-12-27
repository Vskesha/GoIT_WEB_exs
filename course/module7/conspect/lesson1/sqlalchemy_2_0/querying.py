from model_definition import User, session
from sqlalchemy.sql import select


if __name__ == "__main__":
    stmt = select(User)
    print(stmt)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    print("----------------------------------")

    stmt = select(User.id, User.fullname)
    print(stmt)
    result = session.execute(stmt)
    users = []
    for row in result:
        print(row)
        users.append(row)
