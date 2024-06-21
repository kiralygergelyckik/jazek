from Itemek import *
from falu import *
from barat import *
from halal import *
from haz import *
from pap import *
from menu import *
import time
import os
 


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

    
def bevezeto():
    kezdes()
    a = input()
    if a == "1":
        os.system('cls')
        b = halal_menu()
        if b == 1:
            main()
    elif a == "2":
        falu()
    elif a == "3":
        pap()
    elif a == "4":
        haz()
    else:
        if a != "5":
            print("Még mindig számot kell megadni...")
            print("Addig is, itt van ez:")
        barat()

def main():
    menu()
    bevezeto()
main()
