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
    userinfo = relationship('UserInfo', backref='user', uselist=False)


class UserInfo(Base):
    __tablename__ = "userinfo"
    id = Column(Integer(), primary_key=True)
    telegram = Column(String(11))
    phone = Column(String(11))
    site = Column(String(64))
    user_id = Column(Integer(), ForeignKey("users.id"))

if __name__ == "__main__":
    pass
    
