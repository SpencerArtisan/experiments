from user import User
from address import Address
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from base import Base

engine = create_engine('sqlite:///tutorial.db', echo=True)

metadata = Base.metadata
metadata.create_all(engine)

spencer = User("Spencer", "Spencer Ward", "usual")
spencer.addresses = [Address(email_address="sw@hotmail.com")]

Session = sessionmaker(bind=engine)
session = Session()

session.add(spencer)
session.commit()
spencer.password = "changed"
print "*"
print session.dirty

session.commit()

for u, a in session.query(User, Address).filter(User.id==Address.user_id):
    print u,a
