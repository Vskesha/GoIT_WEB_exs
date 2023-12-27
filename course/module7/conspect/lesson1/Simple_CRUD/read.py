from rel_one_to_many import User, Article, session


if __name__ == "__main__":
    user = session.get(User, 1)
    print(user.id, user.name)

    users = session.query(User).all()
    for user in users:
        print(user.id, user.name)

    user1 = session.query(User).filter_by(name="Boris Johnson").first()
    user2 = session.query(User).filter(User.name == "Boris Johnson").scalar()
    print(user1.id, user1.name)
    print(user2.id, user2.name)
