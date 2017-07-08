#!/usr/bin/env python3.4

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

# deklaracja szablonow tabel

class StalDlaEnergetyki(Base):
    __tablename__ = 'STAL_DLA_ENERGETYKI'
    id = Column(Integer, primary_key=True)
    nazwa = Column(String, unique=True)
    minimum_wegla = Column(Float)
    maximum_wegla = Column(Float)
    minimum_manganu = Column(Float)
    maximum_manganu = Column(Float)

class Elektroda(Base):
    __tablename__ = 'ELEKTRODA'
    id = Column(Integer, primary_key=True)
    nazwa = Column(String, unique=True)
    wegiel = Column(Float)
    mangan = Column(Float)

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///orm_in_detail.sqlite')

    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()

    with open('Stal.json', 'r') as f:
        stale = json.load(f)

    for stal in stale:
        obj = StalDlaEnergetyki(**stal)
        s.add(obj)

    with open('Elektroda.json', 'r') as f:
        elektrody = json.load(f)

    for elektroda in elektrody:
        obj = Elektroda(**elektroda)
        s.add(obj)

    s.commit()
