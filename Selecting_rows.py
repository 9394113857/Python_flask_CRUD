from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

s = students.select()
conn = engine.connect()
result = conn.execute(s)

for row in result:
   print (row)

# The WHERE clause of SELECT query can be applied by using Select.where(). For example, if we want to display rows with id >2
# s = students.select().where(students.c.id>2)
