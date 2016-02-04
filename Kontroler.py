#!/usr/bin/env python3

from threading import Thread
from Model import Model
from Zdarzenie import ZdarzenieKoniec, ZdarzenieOblicz
from Strategia import StrategiaKoniec, StrategiaOblicz

class Kontroler(Thread):
    def __init__(self, kolejka_zdarzen, widok, model):
        Thread.__init__(self)
        self._kolejka_zdarzen = kolejka_zdarzen
        self._widok = widok
        self._model = model
        self._stworz_mape_dzialania()

    def _stworz_mape_dzialania(self):
        self._zdarzenie2strategia = {
            type( ZdarzenieKoniec() ) : StrategiaKoniec(self._model),
            type( ZdarzenieOblicz() ) : StrategiaOblicz(self._model),
        }

    def run(self):
        makieta = self._model.pobierz_inicjalizujaca_makiete()
        self._widok.wez_inicjalizujaca_makiete(makieta)
        while True:
            zdarzenie = self._kolejka_zdarzen.get()
            strategia = self._zdarzenie2strategia[type(zdarzenie)]
            try:
                strategia.update(zdarzenie)
            except (Exception) as exc:
                print(exc)
                continue
            if self._model.koniec == True:
                return
            makieta = self._model.pobierz_makiete()
            self._widok.wez_makiete(makieta)

