from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("sqlite:///sqlalchemy_example.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    articles = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer(), primary_key=True)
    title = Column(String(250))
    content = Column(Text())
    user_id = Column(Integer(), ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")


if __name__ == "__main__":
    users = session.query(User).filter_by(name="Peter Miller").all()

    for user in users:
        for article in user.articles:
            print(article.title, user.name)

    article = session.query(Article).filter_by(title="Our country's saddest day").one()
    print(article.title, article.author.name)

