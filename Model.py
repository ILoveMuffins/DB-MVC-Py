#!/usr/bin/env python3.4

from Makieta import Makieta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import *

class Model(object):
    def __init__(self):
        self._engine = create_engine('sqlite:///orm_in_detail.sqlite')
        self._session = sessionmaker(bind=self._engine)
        self._cursor = self._session()
        self._wynikowy_material = None
        self._koniec = False
        self.i = 0 # debug

    def pobierz_pierwsza_makiete(self):
        employees = self._cursor.query(Employee).all()
        makieta = Makieta(employees)
        return makieta

    def pobierz_makiete(self):
        # powinno korzystac z funkcji oblicz wynikowy material
        employees = self._cursor.query(Employee).all()
        makieta = Makieta(employees[self.i])
        self.i = (self.i + 1) % 2
        return makieta

    def oblicz_material(self, materialA, materialB):
        self._wynikowy_material = materialA #zaslepka dla testow

#cursor.execute("SELECT earnings, date FROM table")
#Well, f.eg. you simply do:
#json_string = json.dumps(cursor.fetchall())
#you'll get an array of arrays...:
#    [["earning1", "date1"], ["earning2", "date2"], ...]
