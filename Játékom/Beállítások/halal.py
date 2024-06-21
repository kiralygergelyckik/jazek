import time
def halal_menu():
    print("Mivel meguntad a munkát, ezért nem csinálod tovább.")
    print("Bementél a házadba, de aztán egy egér futott ki a szekrényed alól.")
    print("Ilyedtedben úgy hátraestél, hogy beverted a fejedet az asztalod sarkába.")
    print("mivel kitagadott a családod, akik kihívhatták volna az orvosokat, meghaltál.")
    print()
    time.sleep(5)
    print("Újrapróbálod? (Igen / Nem)")
    a = input("")
    if len(a[0]) == "I" or len(a[0]) == "i" or len(a[1]) == "g" or len(a[1]) == "G":
        print()
        print("Pár másodperc múlva, le lesz generálva az új játékmeneted.")
        time.sleep(4)
        open("Body.py")
    elif len(a[0]) == "n" or len(a[0]) == "N" or len(a[1]) == "e" or len(a[1]) == "E":
        print()
        print("Pár másodperc múlva kiléptetlek.")
        time.sleep(4)
        exit()
    else:
        print()
        print("RAGE QUIT")
        time.sleep(5)
        exit()