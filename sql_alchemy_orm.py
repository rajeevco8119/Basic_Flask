from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sales.db',echo=True)
Base = declarative_base()

class Customers(Base):
    __tablename__= 'customers'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
# Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()


# Inserting in database
def add_customers():
    c1 = Customers(name='Rajeev Mahajan',address='Noida',email='raj.noida@gmail.com')
    session.add(c1)

    session.add_all([
       Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'),
       Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'),
       Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')
    ])
    session.commit()

#add_customers()

# Querying in database
def list_queries():
    result = session.query(Customers).all()
    for row in result:
        print('Name',row.name,"Address",row.address,"Email",row.email)

# list_queries()

# Updating in db
def update():
    x = session.query(Customers).get(2)
    print("Name: ", x.name, "Address:", x.address, "Email:", x.email)
    x.address = 'Banjara Hills Secunderabad'
    session.commit()
    # update({Customers.name:"Mr"+Customers.name},synchronize_session=False)
# update()
# session.rollback() # To rollback all changes, note rollback should happen before commit
# x = session.query(Customers).first()

def filter():
    # Filter operations can be all Aggregate functions (==,!=,>,<)
    result = session.query(Customers).filter(Customers.id>2)
    for row in result:
        print(row.id,row.name,row.email)
# filter()

def filter_like():
    result = session.query(Customers).filter(Customers.name.like('Ra%'))
    for row in result:
        print(row.id,row.name,row.email)
# filter_like()

def filter_in():
    result = session.query(Customers).filter(Customers.id.in_([1,3]))
    for row in result:
        print(row.id, row.name, row.email)
#filter_in()

from sqlalchemy import and_
def filter_and():
    result = session.query(Customers).filter(and_(Customers.id>2,Customers.name.like('Ra%')))
    for row in result:
        print(row.id, row.name, row.email)
# filter_and()

from sqlalchemy import or_
def filter_or():
    result = session.query(Customers).filter(or_(Customers.id>2,Customers.name.like('Ra%')))
    for row in result:
        print(row.id, row.name, row.email)
# filter_or()

def text():
    from sqlalchemy import text
    for cust in session.query(Customers).filter(text("id<3")):
       print(cust.name)

from sqlalchemy import text
def text_function():
    #session.query(Customers).from_statement(text('SELECT * FROM customers')).all()
    stmt = text("SELECT name, id, name, address, email FROM customers")
    stmt = stmt.Columns(Customers.id,Customers.name)
    session.query(Customers.id,Customers.name).from_statement(stmt).all()

# Building relationships
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Invoice(Base):
    __tablename__='invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customers", back_populates="invoices")

Customers.invoices = relationship('Invoice',order_by=Invoice.id,back_populates='customer')
# Base.metadata.create_all(engine)

# Working with Relationship objects
def rel_obj():
    c1 = Customers(name="Gopal Krishna", address="Bank Street Hydarebad", email="gk@gmail.com")
    c1.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]
    session.add(c1)
    session.commit()

def rel_obj2():
    rows = [
        Customers(
            name="Govind Kala",
            address="Gulmandi Aurangabad",
            email="kala@gmail.com",
            invoices=[Invoice(invno=7, amount=12000), Invoice(invno=8, amount=18500)]),

        Customers(
            name="Abdul Rahman",
            address="Rohtak",
            email="abdulr@gmail.com",
            invoices=[Invoice(invno=9, amount=15000),
                      Invoice(invno=11, amount=6000)
                      ])
        ]
    session.add_all(rows)
    session.commit()

# rel_obj2()

# Working woth Joins
def sqlalchemy_joins():
    for c,i in session.query(Customers,Invoice).filter(Customers.id==Invoice.custid).all():
        print("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id, c.name, i.invno, i.amount))

    result = session.query(Customers).join(Invoice).filter(Invoice.amount==3850)
    for row in result:
        for inv in row.invoices:
            print(row.id, row.name, inv.invno, inv.amount)

# sqlalchemy_joins()

# Using functions
from sqlalchemy.sql import func
def sqlalchemy_func():
    stmt = session.query(
        Invoice.custid,func.count('*').label('invoice_count')
    ).group_by  (Invoice.custid).subquery()

    for u, count in session.query(Customers,stmt.c.invoice_count).outerjoin(stmt,Customers.id==stmt.c.custid).order_by(Customers.id):
        print(u.name,count)

    s1 = session.query(Customers).filter(Invoice.invno.__eq__(12))
    s2 = session.query(Customers).filter(Invoice.custid.__ne__(2))
    s3 = session.query(Invoice).filter(Invoice.invno.contains([3,4,5]))
    s4 = session.query(Customers).filter(Customers.invoices.any(Invoice.invno==11))
    s5 = session.query(Invoice).filter(Invoice.customer.has(name='Arjun Pandit'))

# sqlalchemy_func()

# Delete
def delete_load():
    x = session.query(Customers).get(2)
    session.delete(x)
    session.query(Customers).filter_by(name='Gopal Krishna').count()

    session.query(Invoice).filter(Invoice.invno.in_([10, 14])).count()