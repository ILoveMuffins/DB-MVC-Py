#!/usr/bin/env python3.4

from abc import ABCMeta

class Zdarzenie:
    __metaclass__ = ABCMeta

class ZdarzenieOblicz(Zdarzenie):
    def __init__(self, nazwaStaliA=None, nazwaStaliB=None):
        self.nazwaStaliA = nazwaStaliA
        self.nazwaStaliB = nazwaStaliB

class ZdarzenieKoniec(Zdarzenie):
    pass

