from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.sql import select
from sqlalchemy import text

#Creating a database 'college.db'
engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()

#Creating a Students table
students = Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('lastname',String)
)
# meta.create_all(engine)

#Inserting values
conn = engine.connect()
# ins = students.insert().values(name='Ravi',lastname='Mahajan')
# res = conn.execute(ins)

# Execute many commands
# conn.execute(students.insert(),[
#     {'name': 'Rajiv', 'lastname': 'Khanna'},
#     {'name': 'Komal', 'lastname': 'Bhandari'},
#     {'name': 'Abdul', 'lastname': 'Sattar'},
#     {'name': 'Priya', 'lastname': 'Rajhans'},
# ])

# Selecting from table Students
# s = students.select()
# result = conn.execute(s)
# # row = result.fetchall()
# for row in result:
#     print(row)

# Where condition
# s = students.select().where(students.c.id>2)
# result = conn.execute(s)
# row = result.fetchall()
# print(row)

# s = select([students])
# result = conn.execute(s)
# for row in result:
#     print(row)

# Using text to execute query using text
# t = text('SELECT * from students')
# result = conn.execute(t)

# Update
# stmt = students.update().where(students.c.lastname=='Khanna').values(lastname='Bhatt')
# conn.execute(stmt)
# s = students.select()
# conn.execute(s).fetchall()

# from sqlalchemy.sql.expression import update
# stmt = update(students).where(students.c.lastname == 'Khanna').values(lastname = 'Kapoor')

# stmt = students.delete().where(students.c.lastname=='Rajhans')
# conn.execute(stmt)

# addresses = Table(
#    'addresses', meta,
#    Column('id', Integer, primary_key = True),
#    Column('st_id', Integer, ForeignKey('students.id')),
#    Column('postal_add', String),
#    Column('email_add', String))

# meta.create_all(engine)

# conn.execute(addresses.insert(), [
#    {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
#    {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
#    {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
#    {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
#    {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
# ])

# Update query for Multiple tables
# stmt = students.update().values({students.c.name:'xyz',
#                                  addresses.c.email_add:'abc@xyz.com'}).where(students.c.id == addresses.c.id)

# using joins
# from sqlalchemy import join
# from sqlalchemy.sql import select
# j = students.join(addresses,students.c.id==addresses.c.st_id)
# stmt = select([students]).select_from(j)
# result = conn.execute(stmt)
# for res in result:
#     print(res)



