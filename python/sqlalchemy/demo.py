from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
users_table = Table('user', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String)
        )

addresses_table = Table('address', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', None, ForeignKey('user.id')),
        Column('email_address', String, nullable=False)
        )

metadata.create_all(engine)

ins = users_table.insert().values(name='spencer', fullname='Spencer Ward')
conn = engine.connect()

result = conn.execute(ins)


