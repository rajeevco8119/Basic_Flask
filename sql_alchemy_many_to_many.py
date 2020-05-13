from sqlalchemy import create_engine,ForeignKey,Column,Integer,String
engine = create_engine('sqlite:///mycollege.db',echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__= 'department'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    employees = relationship('Employee',secondary='link')

class Employee(Base):
    __tablename__='employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    departments = relationship('Department', secondary='link')

class Link(Base):
    __tablename__='link'
    department_id = Column(
        Integer,
        ForeignKey('department.id'),
        primary_key=True
    )
    employee_id = Column(Integer,
                         ForeignKey('employee.id'),
                         primary_key=True)
Base.metadata.create_all(engine)

d1 = Department(name='Accounts')
d2 = Department(name='Sales')
d3 = Department(name='Marketing')

e1 = Employee(name='John')
e2 = Employee(name='Tony')
e3 = Employee(name='Graham')

# Appending values
e1.departments.append(d1)
e2.departments.append(d3)
d1.employees.append(e3)
d2.employees.append(e2)
d3.employees.append(e1)
e3.departments.append(d2)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

def add():
    session.add(e1)
    session.add(e2)
    session.add(d1)
    session.add(d2)
    session.add(d3)
    session.add(e3)
    session.commit()

add()
def display():
    for x in session.query(Department,Employee).filter(Link.department_id==Department.id,
                                                       Link.employee_id==Employee.id).order_by(Link.department_id).all():
        print("Department: {} Name: {}".format(x.Department.name,x.Employee.name))
