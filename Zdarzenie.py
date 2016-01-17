#!/usr/bin/env python3.4

from abc import ABCMeta
class Zdarzenie:
    __metaclass__ = ABCMeta

class ZdarzenieOblicz(Zdarzenie):
    def __init__(self, stalA=None, stalB=None):
        self._stalA = stalA
        self._stalB = stalB

class ZdarzenieKoniec(Zdarzenie):
    pass

