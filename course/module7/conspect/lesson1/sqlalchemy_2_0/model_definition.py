from sqlalchemy import (
    create_engine,
    Integer,
    String,
    ForeignKey,
    select,
    Text,
    and_,
    desc,
    func,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship,
    Mapped,
    mapped_column,
)

engine = create_engine("sqlite:///test_sqlalchemy_2_0.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column("user_id", Integer, ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")


Base.metadata.create_all(engine)


if __name__ == "__main__":
    names = ["Crystal Najera", "Shaun Beck", "Kathrin Reinhardt"]
    for name in names:
        user = User(fullname=name)
        session.add(user)
    session.commit()
