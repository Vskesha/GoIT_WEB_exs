from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("sqlite:///sqlalchemy_example.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))
    person = relationship(Person)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    new_person = Person(name="Bill")
    session.add(new_person)

    session.commit()

    new_address = Address(post_code="00000", person=new_person)
    session.add(new_address)
    session.commit()

    for person in session.query(Person).all():
        print(person.name)
