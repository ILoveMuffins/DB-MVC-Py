#!/usr/bin/env python3.4

from abc import ABCMeta
class Zdarzenie:
    __metaclass__ = ABCMeta

class ZdarzenieOblicz(Zdarzenie):
    def __init__(self, materialA=None, materialB=None):
        self._materialA = materialA
        self._materialB = materialB

class ZdarzenieKoniec(Zdarzenie):
    pass

