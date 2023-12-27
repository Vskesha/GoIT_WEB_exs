from model_definition import User, session
from sqlalchemy.sql import select, and_

if __name__ == "__main__":
    separator = "-------------------------------\n"
    stmt = select(User).where(User.fullname == "Shaun Beck")
    print(stmt)
    result = session.execute(stmt).scalar_one()
    print(result.id, result.fullname)
    print(separator)

    stmt = select(User).where(User.fullname.like("%ha%"))
    print(stmt)
    result = session.execute(stmt)
    for user in result.scalars().all():
        print(user.id, user.fullname)
    print(separator)

    stmt = select(User).where(
        and_(User.fullname.like("%ha%"), User.fullname != "Shaun Beck")
    )
    print(stmt)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)
    print(separator)

    stmt = select(User).where(User.fullname.like("%ha%")).where(User.fullname != "Shaun Beck")
    print(stmt)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)
    print(separator)
