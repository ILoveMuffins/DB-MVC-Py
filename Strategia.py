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
        materialA = zdarzenie._materialA
        materialB = zdarzenie._materialB
        warunek1 = materialA != None and materialB != None
        warunek2 = materialA != '' and materialB != ''
        if warunek1 and warunek2:
            self._model.oblicz_material(materialA, materialB)
        else:
            raise Exception('plik: Strategia.py, wyjatek: jeden z materialow \
jest None badz string pusty')

class StrategiaKoniec(Strategia):
    def update(self, zdarzenie):
        self._model._koniec = True

