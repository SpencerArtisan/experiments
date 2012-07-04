from demo import users_table, engine
from sqlalchemy.sql import select

connection = engine.connect()
s = select([users_table.c.name])
result = connection.execute(s)

for row in result:
    print row
