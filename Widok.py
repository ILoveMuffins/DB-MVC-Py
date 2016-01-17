#!/usr/bin/env python3.4

from Gui import Gui
from Zdarzenie import ZdarzenieKoniec, ZdarzenieOblicz

class Widok(object):
    def __init__(self, root, kolejka_zdarzen):
        self._kolejka_zdarzen = kolejka_zdarzen
        self.root = root
        self._gui = Gui(self, root) # gui dostaje odniesienie do parenta
            # aby gui moglo wywolac metode generuj_zdarzenie_oblicz
        self._gui.pack(side='top', fill='both', expand=True)

    def wez_makiete(self, makieta):
        self._gui.update(makieta)

    def wez_pierwsza_makiete(self, makieta):
        self._gui.pierwsze_update(makieta)

    def _obsluz_zamkniecie_gui(self):
        self._kolejka_zdarzen.put(ZdarzenieKoniec())
        self.root.destroy()

    def generuj_zdarzenie_oblicz(self):
        materialA = self._gui._comboBox.get()
        materialB = self._gui._comboBox2.get()
        self._kolejka_zdarzen.put(ZdarzenieOblicz(materialA, materialB))

