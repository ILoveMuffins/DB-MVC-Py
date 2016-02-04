#!/usr/bin/env python3.4

from abc import abstractmethod, ABCMeta

class Strategia:
    __metaclass__ = ABCMeta # deklaracja abstrakcyjnej klasy

    def __init__(self, model):
        self._model = model

    @abstractmethod
    def update(self, zdarzenie):
        pass

class StrategiaOblicz(Strategia):
    def update(self, zdarzenie):
        nazwaStaliA = zdarzenie.nazwaStaliA
        nazwaStaliB = zdarzenie.nazwaStaliB
        warunek1 = nazwaStaliA != None and nazwaStaliA != ''
        warunek2 = nazwaStaliB != None and nazwaStaliB != ''
        if warunek1 and warunek2:
            self._model.oblicz(nazwaStaliA, nazwaStaliB)
        else:
            raise Exception('plik: Strategia.py, wyjatek: nazwa stali jest None badz string pusty')

class StrategiaKoniec(Strategia):
    def update(self, zdarzenie):
        self._model.koniec = True

