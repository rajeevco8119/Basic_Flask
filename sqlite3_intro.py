import sqlite3
conn = sqlite3.connect('company.db')
curs = conn.cursor()

#SQL query to create table Employee in company.db
curs.execute('create table employee (name,age)')

##SQL query to create table Book in company.db
#curs.execute('create table book (name,price)')

#DML operation-Insert
curs.execute("insert into book values ('song',750)")

#DML operation- Insert
curs.execute("insert into employee values ('Ali',25)")

values = [('Brad',54),('Ross',34),('Muhamad',28)]

#Inserting more than 1 value
curs.executemany('insert into employee values (?,?)',values)

#DDL display operation
curs.execute('select * from book')

#DDL fetch operation
all_emp= curs.fetchone()
print(all_emp)

conn.commit()

#Closing the connection
conn.close()
