#!/bin/bash

# zaklada zainstalowany python interpreter, oraz sqlite

#sudo apt-get install postgresql # instalacja systemu zarzadzania bazami danych
#sudo update-rc.d -f postgresql remove # wylaczenie automatycznego uruchamiania bazy danych wraz ze startem systemu
#sudo service postgresql start # uruchomienie systemu zarzadzania bazami danych
#sudo -u postgres psql postgres # logowanie sie do SZBD(DBMS) na uzytkownika: postgres haslo: postgres
#create database baza_danych # tworzenie nowej bazy danych o nazwie 'baza_danych'
#sudo service postgresql stop # zatrzymanie SZDB

sudo apt-get install python3-tk # instalacja tkinter
virtualenv venv # stworzenie wirtualnego srodowiska
source venv/bin/activate # uruchomienie wirtualnego srodowiska
sudo apt-get install python3-pip # instalacja managera pakietow pythona3 - pip3
# pip3 install psycopg2 # instalacja adaptera postgresql dla python
pip3 install --user sqlalchemy # instalacja Python ORM
deactivate # wylaczenie wirtualnego srodowiska

