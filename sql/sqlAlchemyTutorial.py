#!/usr/bin/python3

# This is a documentation
# Headings have one (#) and children follow subsequently, so h2 -> ##, h3 -> ### etc

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Create the Engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Create the Base to define the database schema
Base = declarative_base()

# Create a table


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname
        )

# Create a schema
Base.metadata.create_all(engine)

# Create an Instance of the mapped class
Panda_user = User(name="Panda", fullname="Panda 787", nickname="Panda T")
print("Name: {}".format(Panda_user.name))
print("Nickname: {}".format(Panda_user.nickname))

# Create a sesssion
# (Note:) Sessions are used to 'talk' with the db

Session = sessionmaker(bind=engine)

# (Note): Whenever you want to talk to the db, you instantiate a session
session = Session()

## Adding and Updating objectts
session.add(Panda_user)

## Querying the Database
our_user = session.query(User).filter_by(name="Panda").first()
print(our_user)

## Adding More Users
session.add_all([
    User(name="Wendy", fullname="Wendy Williams", nickname="Windy"),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')
])

## Pushing your changes to the database is done through a process called flushing
session.commit()