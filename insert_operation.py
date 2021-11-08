from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

ins = students.insert()
ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
conn = engine.connect()
result = conn.execute(ins)

# result.inserted_primary_key
# [1]

# To issue many inserts using DBAPI’s execute many() method,
# we can send in a list of dictionaries each containing a distinct set of parameters to be inserted.

# conn.execute(students.insert(), [
#    {'name':'Rajiv', 'lastname' : 'Khanna'},
#    {'name':'Komal','lastname' : 'Bhandari'},
#    {'name':'Abdul','lastname' : 'Sattar'},
#    {'name':'Priya','lastname' : 'Rajhans'},
# ])