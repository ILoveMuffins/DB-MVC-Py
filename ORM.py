#!/usr/bin/env python3.4

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

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

    # wypelnianie bazy danych danymi
    # stale

    stal1 = StalDlaEnergetyki(nazwa="St36K", minimum_wegla=0.08, maximum_wegla=0.016,
minimum_manganu=0.4, maximum_manganu=1.6)
    stal2 = StalDlaEnergetyki(nazwa="St41K", minimum_wegla=0.12, maximum_wegla=0.2,
minimum_manganu=0.45, maximum_manganu=1.6)
    stal3 = StalDlaEnergetyki(nazwa="St44K", minimum_wegla=0.14, maximum_wegla=0.22,
minimum_manganu=0.55, maximum_manganu=1.6)
    stal4 = StalDlaEnergetyki(nazwa="15", minimum_wegla=0.12, maximum_wegla=0.18,
minimum_manganu=0.3, maximum_manganu=0.8)
    stal5 = StalDlaEnergetyki(nazwa="20G", minimum_wegla=0.17, maximum_wegla=0.24,
minimum_manganu=0.7, maximum_manganu=1)
    stal6 = StalDlaEnergetyki(nazwa="16M", minimum_wegla=0.12, maximum_wegla=0.2,
minimum_manganu=0.5, maximum_manganu=0.8)
    stal7 = StalDlaEnergetyki(nazwa="13HMF", minimum_wegla=0.1, maximum_wegla=0.18,
minimum_manganu=0.4, maximum_manganu=0.7)
    stal8 = StalDlaEnergetyki(nazwa="10H2M", minimum_wegla=0.08, maximum_wegla=0.15,
minimum_manganu=0.4, maximum_manganu=0.6)
    stal9 = StalDlaEnergetyki(nazwa="25", minimum_wegla=0.22, maximum_wegla=0.3,
minimum_manganu=0.4, maximum_manganu=0.7)
    stal10 = StalDlaEnergetyki(nazwa="35", minimum_wegla=0.32, maximum_wegla=0.39,
minimum_manganu=0.5, maximum_manganu=0.8)
    stal11 = StalDlaEnergetyki(nazwa="45", minimum_wegla=0.45, maximum_wegla=0.5,
minimum_manganu=0.5, maximum_manganu=0.8)
    stal12 = StalDlaEnergetyki(nazwa="25HM", minimum_wegla=0.22, maximum_wegla=0.29,
minimum_manganu=0.4, maximum_manganu=0.7)
    stal13 = StalDlaEnergetyki(nazwa="35HM", minimum_wegla=0.34, maximum_wegla=0.4,
minimum_manganu=0.4, maximum_manganu=0.7)
    stal14 = StalDlaEnergetyki(nazwa="26H2MF", minimum_wegla=0.22, maximum_wegla=0.3,
minimum_manganu=0.3, maximum_manganu=0.6)
    stal15 = StalDlaEnergetyki(nazwa="21HMF", minimum_wegla=0.17, maximum_wegla=0.35,
minimum_manganu=0.5, maximum_manganu=0.5)
    stal16 = StalDlaEnergetyki(nazwa="20HMFTB", minimum_wegla=0.17, maximum_wegla=0.24,
minimum_manganu=0, maximum_manganu=0.5)

    s.add(stal1)
    s.add(stal2)
    s.add(stal3)
    s.add(stal4)
    s.add(stal5)
    s.add(stal6)
    s.add(stal7)
    s.add(stal8)
    s.add(stal9)
    s.add(stal10)
    s.add(stal11)
    s.add(stal12)
    s.add(stal13)
    s.add(stal14)
    s.add(stal15)
    s.add(stal16)

    # elektrody
    e1 = Elektroda(nazwa="OK74.46", wegiel=0.06, mangan=0.75)
    e2 = Elektroda(nazwa="OK76.16", wegiel=0.07, mangan=0.6)
    e3 = Elektroda(nazwa="OK76.18", wegiel=0.07, mangan=0.6)
    e4 = Elektroda(nazwa="OK76.26", wegiel=0.07, mangan=0.65)
    e5 = Elektroda(nazwa="OK76.28", wegiel=0.07, mangan=0.7)
    e6 = Elektroda(nazwa="OK76.35", wegiel=0.07, mangan=0.7)
    e7 = Elektroda(nazwa="OK76.98", wegiel=0.1, mangan=0.8)

    s.add(e1)
    s.add(e2)
    s.add(e3)
    s.add(e4)
    s.add(e5)
    s.add(e6)
    s.add(e7)

    s.commit()

