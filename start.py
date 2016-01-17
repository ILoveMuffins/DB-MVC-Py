#!/usr/bin/env python3.4

from Model import Model
from Kontroler import Kontroler
from Widok import Widok
from queue import Queue
import tkinter

model = Model()
root = tkinter.Tk()
kolejka_zdarzen = Queue()
widok = Widok(root, kolejka_zdarzen)
kontroler = Kontroler(kolejka_zdarzen, widok, model)
kontroler.start()
root.mainloop()
kontroler.join()

