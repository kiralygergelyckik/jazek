import time
import os

def halal_menu():
    os.system('cls')
    print("Pár percig még dolgoztál, de véleményed nem változott. Még mindig unatkozol.")
    print("Bementél hát a házadba, de aztán egy egér futott ki a szekrényed alól.")
    print("Ilyedtedben úgy hátraestél, hogy beverted a fejedet az asztalod sarkába.")
    print("mivel kitagadott a családod, akik kihívhatták volna az orvosokat, meghaltál.")
    print()
    time.sleep(5)
    print("Megölt egy egér. lol")
    print()
    print("Újrapróbálod? (Igen / Nem)")
    a = input("")
    b = igen_nem(a)
    return b
    
def igen_nem(b):
    if b[0] == "I" or b[0] == "i" or b[1] == "g" or b[1] == "G":
        print()
        print("Pár másodperc múlva, le lesz generálva az új játékmeneted.")
        time.sleep(4)
        return 1  
    elif b[0] == "n" or b[0] == "N" or b[1] == "e" or b[1] == "E":
        print()
        print("Pár másodperc múlva kiléptetlek.")
        time.sleep(4)
        return 2
    else:
        print()
        print("RAGE QUIT")
        time.sleep(5)
        exit()
