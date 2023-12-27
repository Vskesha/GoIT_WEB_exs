from model_definition import User, Post, session
from sqlalchemy import func, select


if __name__ == '__main__':
    stmt = select(User.fullname, func.count(Post.id)).join(Post).group_by(User.fullname)
    print(stmt)
    result = session.execute(stmt).all()
    for name, count in result:
        print(f"{name} has {count} posts")
