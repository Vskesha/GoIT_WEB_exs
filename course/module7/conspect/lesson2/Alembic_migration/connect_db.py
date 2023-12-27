from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///mynotes.db")
Session = sessionmaker(bind=engine)
session = Session()
