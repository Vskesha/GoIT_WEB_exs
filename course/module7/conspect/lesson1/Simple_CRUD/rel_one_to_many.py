from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Text


engine = create_engine("sqlite:///test_one_to_many.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    articles = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(Text)
    user_id = Column(Integer(), ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")


Base.metadata.create_all(engine)
Base.metadata.bind = engine
