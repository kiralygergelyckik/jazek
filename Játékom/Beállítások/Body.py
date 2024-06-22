from Itemek import *
from falu import *
from barat import *
from halal import *
from haz import *
from bugfix import *
from papsag import pap
from menu import *
import time
import os
from random import *

def valasztas(lehetoseg):
    a = input("")   
    if a == "1" and lehetoseg >= 1:
        valasz = 1
    elif a == "2" and lehetoseg >= 2:
        valasz = 2
    elif a == "3" and lehetoseg >= 3:
        valasz = 3
    elif a == "4" and lehetoseg >= 4:
        valasz = 4
    elif a == "5" and lehetoseg >= 5:
        valasz = 5
    else:
        valasz = randrange(1, len(lehetoseg))
        print()
        print("Mi olyan nehéz egy szám beírásában?")
        print("Mindegy, döntök helyetted én!")
        print(f"A döntésem a(z) {a}. választásra jutott!")
        time.sleep(7)
        print()
    return valasz


def pontok(pontszam):
    if pontszam == 0:
        print("Te egy igazi legenda vagy, mint Gergely")
        print("Ha Gergely nem is, de én büszke vagyok rád. :3")
    elif pontszam == 1 or pontszam == 2:
        print("Majdnem sikerült úgy bejárnod az utat, mint Gergely.")
        print("Kis gyakorlással, akár legenda is válhat belőled.")
    elif pontszam > 2 and pontszam < 5:
        print("Átlagos vagy.")
        print("Úgy gondolkodsz, mit egy átlag ember")
    elif 5 < pontszam and pontszam < 9:
        print("Hát, rád férne egy kevés barát.")
        print("És óvatosan próbálj meg legendává válni.")
        print("Nagyon sok gyakorlás vár rád.")
    else:
        print("Ne maradj egyedül, mert meghalsz.")
        print("Nálad komoly problémák vannak, ne menj a természetbe.")
        print("LoL-oz csak tovább.")
    time.sleep(10)
    exit()
        
def menu():
    bevezetes()
    kezdhetjuk = input()
    if kezdhetjuk != "1":
        print()
        print("1 dolgod volt ): Szó szerint 1.")
        print("Na én veled nem szórakozok, úgyhogy kezjük.")
        time.sleep(5)
    else:
        print()
        print("Akkor kezdjünk is bele.")
        time.sleep(3)
    os.system('cls')

    
def bevezeto(pontszam):
    kezdes()
    a = valasztas(5)
    if a == 1:
        b = halal_menu()
        if b == 1:
           main(pontszam) 
           os.system('cls')
        elif b == 2:
            exit()
    elif a == 2:
        falu()
    elif a == 3:
        pap()
    elif a == 4:
        haz()
    elif a == 5:
        barat()

def main(pontszam):
    pontszam += 1
    menu()
    bevezeto(pontszam)
        
main(pontszam)

