from model_definition import User, Post, session
from sqlalchemy.sql import select, func


if __name__ == "__main__":
    stmt = select(User.id, User.fullname)
    print(stmt)
    result = session.execute(stmt)
    users = []
    for row in result:
        users.append(row)

    for user in users:
        post = Post(
            title=f"Title {user[1]}",
            body=f"Body post user {user[1]}",
            user_id=user[0]
        )
        session.add(post)
    session.commit()
