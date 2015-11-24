#!/usr/bin/env python3.4

# tak sie robi dla postgresql'a
#engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
# ogolnie:
#dialect+driver://username:password@host:port/database

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# deklaracja szablonow tabel

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                         uselist=True,
                         cascade='delete,all'))

# wypelnianie bazy danych danymi

if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///orm_in_detail.sqlite')

    from sqlalchemy.orm import sessionmaker
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)

    d = Department(name="IT")
    emp1 = Employee(name="John", department=d)
    emp2 = Employee(name="Gzyms", department=d)
    s = session()
    s.add(d)
    s.add(emp1)
    s.add(emp2)
    s.commit()
    for a in s.query(Employee).all():
        print(a.name, a.hired_on, a.department_id)
    #s.delete(d)  # Deleting the department also deletes all of its employees.
    #s.commit()
    #print(s.query(Employee).all())

