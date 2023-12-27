from model_definition import User, session
from sqlalchemy.sql import select, desc, asc


if __name__ == '__main__':
    separator = "-------------------------------\n"
    stmt = select(User).order_by(User.fullname)
    print(stmt)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)
    print(separator)

    stmt = select(User).order_by(desc(User.fullname))
    print(stmt)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)
    print(separator)

    