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
        self._wynik = None
        self._koniec = False

    def pobierz_pierwsza_makiete(self):
        stale = self._cursor.query(StalDlaEnergetyki).all()
        makieta = Makieta(stale)
        return makieta

    def pobierz_makiete(self):
        makieta = Makieta(self._wynik, self._min_mn, self._max_mn)
        return makieta

    def oblicz(self, nazwaStaliA, nazwaStaliB):
        stalA = self._wczytaj_stal(nazwaStaliA)
        stalB = self._wczytaj_stal(nazwaStaliB)

        self._min_mn, self._max_mn = self._oblicz_przeciecie_zawartosci_manganu(stalA, stalB)

        warunek = and_(Elektroda.mangan>=self._min_mn, Elektroda.mangan<=self._max_mn)
        znalezioneElektrody = self._cursor.query(Elektroda).filter(warunek).all()

        self._wynik = znalezioneElektrody

    def _wczytaj_stal(self, nazwaStali):
        return self._cursor.query(StalDlaEnergetyki).filter_by(nazwa=nazwaStali).one()

    def _oblicz_przeciecie_zawartosci_manganu(self, stalA, stalB):
        min_mn = max(stalA.minimum_manganu, stalB.minimum_manganu)
        max_mn = min(stalA.maximum_manganu, stalB.maximum_manganu)
        return min_mn, max_mn

