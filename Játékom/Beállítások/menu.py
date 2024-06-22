import os
def bevezetes():
    os.system('cls')
    print()
    print()
    print("Üdvözöllek!")
    print("Ebben a játékban végigmehetsz Gergely legendás útján.")
    print("De vajon sikerül végigvinned, vagy meghalsz benne, mint mindenki más? Most kiderül!")
    print("Készen állsz?")
    print("A folytatáshoz nyomj egy 1-est!")

def kezdes(a=0, b=0, falu=0, pap=0, haz=0, barat=0):
    if b == 0:
        print("Egyszer, réges-régen, élt egy ember, kinek neve Gergely volt.")
        print("Körülbelül, 1617-ben, március 14-én, 11 óra, 12. percében és annak 3. másodpercében, éppen a házimunkáját csinálta, amit megunt.")
        print("Így hát kalandra indult, de vajon hova?")
        print("Te hova mennél a helyébe? (Számokkal jelöld válaszod)")
    if a == 0:
        print()
        print("1 - Tovább csinálom a házimunkát.")
        if falu==0:
            print("2 - Elmegyek, körbenézek a közeli faluban.")
        if pap==0:    
            print("3 - Beállok szerzetesnek.")
        if haz==0:
            print("4 - Bemegyek a házamba.")
        if barat==0:
            print("5 - Megkeresem a barátaimat, hátha van kedvük valamit csinálni.")
