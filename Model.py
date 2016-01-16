#!/usr/bin/env python3.4

from Makieta import Makieta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import *
from sqlalchemy.orm import load_only
from sqlalchemy import and_

class Model(object):
    def __init__(self):
        self._engine = create_engine('sqlite:///orm_in_detail.sqlite')
        self._session = sessionmaker(bind=self._engine)
        self._cursor = self._session()
        self._wynikowy_material = None
        self._koniec = False
        self.i = 0 # debug

    def pobierz_pierwsza_makiete(self):
        stale = self._cursor.query(StalDlaEnergetyki).all()
        makieta = Makieta(stale)
        return makieta

    def pobierz_makiete(self):
        makieta = Makieta(self._wynikowy_material)
        return makieta

    def oblicz_material(self, materialA, materialB):
        A_min_mang = None
        A_max_mang = None
        B_min_mang = None
        B_max_mang = None
        for a in self._cursor.query(StalDlaEnergetyki).filter_by(nazwa=materialA):
            A_min_mang = a.minimum_manganu
            A_max_mang = a.maximum_manganu
        for a in self._cursor.query(StalDlaEnergetyki).filter_by(nazwa=materialA):
            B_min_mang = a.minimum_manganu
            B_max_mang = a.maximum_manganu
        obliczony = None
        for a in self._cursor.query(Elektroda).filter(and_(and_(Elektroda.mangan>=A_min_mang, Elektroda.mangan<=A_max_mang), and_(Elektroda.mangan>=B_min_mang, Elektroda.mangan<=B_max_mang))):
            obliczony = a
            print("--->", str(a.nazwa))

        self._wynikowy_material = obliczony #zaslepka dla testow



