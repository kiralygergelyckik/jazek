import os
import time
from Itemek import *
from bugfix import *
from random import randint

zold = '\033[32m'
RESET = '\033[0m'

def pap_halal_menu():
    from halal import halal_menu
    b = halal_menu()
    if b == 1:
        from Body import main, pontszam
        main(pontszam+1) 
        os.system('cls')
    elif b == 2:
        exit()

def mit_szeretnetek():
    os.system('cls')
    print("Jó napot Uram! Egyedül volt a templomban?")
    print()
    print("1 - Igen, egyedül voltam!")
    print("2 - Mesélsz nekik a hangról.")
    print("3 - elmenekülsz.")
    a = valasztas(3)
    os.system('cls')
    if a == 1:
        print("Igen, egyedül voltam, miért?")
        print()
        print('"Tudja, valaki megölte ezt a papot."')
        print('"Tudja, ez a pap elrabolt pár gyermeket, akiket rituáékra használt fel."')
        print('"Biztos nem látott semmit?"')
        print()
        print("1 - igen, biztos!")
        print("2 - Én voltam!")
        s = valasztas(2)
        if s == 1:
            print("A lovagok tovább sétáltak, te visszasétáltál a birtokodhoz.")
            from menu import kezdes
            kezdes(0, 1, 0, 1, 0, 0)
            kezdeti_nehezseg()
        elif s == 2:
            print("A lovagok fél percig néztek téged.")
            time.sleep(2)
            print("Ezután az egyik előhúzta a kardját és leszúrt.")
            time.sleep(2)
            print("Miközben sötétség vesz körül, ennyit hallasz:")
            time.sleep(2)
            print()
            print('"Megölte a szekta vezért, most mi legyen?"')
            time.sleep(2)
            print()
            print("Újra próbálod?")
            print()
            print("1 - Igen, megpróbálom mégegyszer!")
            print("2 - Most léptes ki.")
            a = valasztas(2)
            time.sleep(3)
            if a == 1:
                from Body import main, pontszam
                main(pontszam+1)
            elif a == 2:
                exit()        
    elif a == 2:
        os.system('cls')
        print("Egy gyermek hangot hallottam a templomból.")
        print()
        print("A lovagok egymásra néztek, majd bementek a templomba.")
        print()
        print("Mit csinálsz?")
        print("1 - Hazamegyek.")
        print("2 - Utánuk megyek.")
        s = valasztas(2)
        os.system('cls')
        if s == 1:
            os.system('cls')
            print("Inkább hazaindultál.")
            print()
            print("Újra a birtokodon találod magad, hogyan tovább?")
            print()
            from menu import kezdes
            kezdes(0,1,0,0,0,0)
            kezdeti_nehezseg()
        elif s == 2:
            print("Utánuk mentél, ők nem vették észre.")
            print("Az oltárhoz mentek, majd elfordultak jobbra egy folyosóhoz.")
            time.sleep(6)
            print("Követted őket, de a folyosó egyszer csak végetért.")
            print("Halk nyögéseket hallasz, majd a fal kinyílik elötted.")
            print("A fal másik végénél a két lovagot látod, egy halott kislánnyal.")
            print("Mire megnézted volna, az egyik suhintott egyet a kardjával.")
            time.sleep(8)
            print()
            print("Újra próbálod?")
            print()
            print("1 - Igen, megpróbálom mégegyszer!")
            print("2 - Most léptes ki.")
            a = valasztas(2)
            time.sleep(3)
            if a == 1:
                from Body import main, pontszam
                main(pontszam+1)
            elif a == 2:
                exit()        
    elif a == 3:
        os.system('cls')
        print()
        print("Gyorsan megpróbálsz elmenekülni.")
        print("Már egy ideje futsz, aztán egy nyilat érzel a hátadban.")
        print("Elvéreztél.")
        time.sleep(2)
        print()
        print("Újra próbálod?")
        print()
        print("1 - Igen, megpróbálom mégegyszer!")
        print("2 - Most léptes ki.")
        a = valasztas(2)
        time.sleep(3)
        if a == 1:
            from Body import main, pontszam
            main(pontszam+1)
        elif a == 2:
            exit()        

def papsag():
    os.system('cls')
    print('"Jaj, Fiam! Papnak állni csak így nem lehet."')
    print("Csak a legtisztább szívűek léphetnek be.")
    print()
    print('1 - "Készen állok!"')
    print("2 - Leszúrod")
    a = valasztas(2)
    os.system('cls')
    if a ==1:
        print("Hát, akkor nézzük meg!")
        print("A pap valami furcsa mozdulatokat kezd el kántálni.")
        print("Kezében hírtelen fehér fény jelent meg.")
        print("Rádmutatott és a fehér fény átjárta testedet.")
        print()
        i, j, k = 0, 0, 0
        while i < len(tulajdonsag) and tulajdonsag[i] != "karizma":
            i += 1
        if i < len(tulajdonsag):
            while j < len(tulajdonsag) and tulajdonsag[j] != "jószívű":
                j += 1
            if j < len(tulajdonsag):
                    while k < len(tulajdonsag) and tulajdonsag[k] != "Népi hős":
                        k += 1
                    if k < len(tulajdonsag):
                        print("A fehér fény átjárja tested.")
                        print("Hirtelen melegség áraszt el.")
                        print("A pap szép lassan elkezd rád mosolyogni.")
                        print("Egy óriási nagy fényből készült kard esik le az égről.")
                        print("A kard ráesett a papra, Isten elultizott.")
                        print("Hirtelen páncél termett rajtad.")
                        print("Megkaptad az isteni tulajdonságaidat!")
                        time.sleep(15)
                        os.system('cls')
                        print(zold + "+ Passzív: Gyógyulsz csatán kívül." + RESET)
                        time.sleep(3)
                        print(zold + "+ Megnőt a gyorsaságod, egy hatalmasat ráütsz az ellenségedre a kardoddal." + RESET)
                        time.sleep(3)
                        print(zold + "+ Pajzsot kapsz pár másodpercre." + RESET)
                        time.sleep(3)
                        print(zold + "+ Pörögni kezdesz, miközben a kardoddal rengeteget sebzesz." + RESET)
                        time.sleep(3)
                        print(zold + "+ Egy hatalmas fénykard jön le az égből, akire csak akarod." + RESET)
                        time.sleep(15)
                        os.system('cls')
                        print("Gratulálunk, végigvitted az utad! Mint Gergely")
                        print("Értékelésed:")
                        time.sleep(3)
                        from Body import pontok
                        pontok(pontszam)
                        time.sleep(15)
                    else:
                        print("Már nagyon közel vagy, de még nem állsz készen!")
                        pap_valasztas()
            else:
                print("Még nem állsz készen, de tudod merre vezet utad!")
                pap_valasztas()
        else:
            print("Még nem állsz készen")
            pap_valasztas()                                        
    elif a == 2:
        leszur()

def kezdeti_nehezseg():
    a = valasztas(4)
    os.system('cls')
    if a == 1:
        pap_halal_menu()
    elif a == 2:
        from falu import falu
        falu()
    elif a == 3:
        print("Ez csak fölösleges halálhoz vezetne.")
        menekul()
    elif a == 4:
        from haz import haz
        haz()
    elif a == 5:
        from barat import barat
        barat()

def otthagy():
    os.system('cls')
    print("Inkább szó nélkül visszafordultál.")
    print()
    print("Újra a birtokodon találod magad, hogyan tovább?")
    print()
    from menu import kezdes
    kezdes(0,1,0,0,0,0)
    kezdeti_nehezseg()
    
def menekul():
    from menu import kezdes
    print()
    print("Visszamenekültél a birtokodba.")
    print("Most már tudod, hogy köröznek. Mit teszel?")
    print()
    kezdes(0,1,0,1,0,0)
    kezdeti_nehezseg()
    
def templom_elott():
    os.system('cls')
    i = 0
    print("Kimentél a templomból.")
    print("A pap eltűnt, csak egy kis vér mennyiség maradt a földön.")
    print("Miközben töprengtél a történteken, hangokat hallasz közeledni.")
    print("Éppen menekültél volna, mikor kettő őr megállított.")
    print()
    print("Mit teszel?")
    print()
    print("1 - Harcolok velük!")
    print("2 - Elmenekülök.")
    print("3 - Megkérdezem mit szeretnének.")
    while i < len(targyak) and targyak[i] != "kés" and targyak[i] != "kard":
        i += 1
    if i < len(targyak):
        print(f"4 - Előveszem a {targyak[i]} nevezetű tárgyamat és leszúrom őket.")
        s = True
        a = valasztas(4)
    else:
        a = valasztas(3)
    if a == 1:
        r = randint(1, 10)
        if r >= 5:
            os.system('cls')
            print("Nehezen, de kiütötted őket ököllel.")
            print()
            print("Mi teszel?")
            print()
            print("1 - Elmenekülök.")
            print("2 - Megnézem, van-e náluk valami.")
            a = valasztas(2)
            if a == 1:
                menekul()
            elif a == 2:
                print("Az első lovagnál találtál egy kardot!")
                print("Mikor a másik lovag nyúltál volna, leszúrtak egy tőrrel.")
                print("Az előző lovag volt az. Meghaltál.")
                print()
                print("Újra próbálod?")
                print()
                print("1 - Igen, megpróbálom mégegyszer!")
                print("2 - Most léptes ki.")
                a = valasztas(2)
                time.sleep(3)
                if a == 1:
                    from Body import main, pontszam
                    main(pontszam+1)
                elif a == 2:
                    exit()
        else:
            os.system('cls')
            print("Neki mentél az egyiknek, aki pofán vágott, majd a másik leszúrt.")
            print("Meghaltál.")
            print()
            print("Újra próbálod?")
            print()
            print("1 - Igen, megpróbálom mégegyszer!")
            print("2 - Most léptes ki.")
            a = valasztas(2)
            time.sleep(3)
            if a == 1:
                from Body import main, pontszam
                main(pontszam+1)
            elif a == 2:
                exit()
    elif a == 2:
        menekul()
    elif a == 3:
        mit_szeretnetek()
    elif a == 4 and s== True:
        print("Nehezen, de leszúrtad őket.")
        print()
        print("Mi teszel?")
        print()
        print("1 - Elmenekülök.")
        print("2 - Megnézem, van-e náluk valami.")
        a = valasztas(2)
        if a == 1:
            menekul()
        elif a == 2:
            print("Az első lovagnál találtál egy kardot!")
            print("Mikor a másik lovag nyúltál volna, leszúrtak egy tőrrel.")
            print("Az előző lovag volt az. Meghaltál.")
            print()
            print("Újra próbálod?")
            print()
            print("1 - Igen, megpróbálom mégegyszer!")
            print("2 -Most léptes ki.")
            a = valasztas(2)
            time.sleep(3)
            if a == 1:
                from Body import main, pontszam
                main(pontszam+1)
            elif a == 2:
                exit()

def siras():
    os.system('cls')
    print("Megnézted mégegyszer, és találtál egy fáklyát a falon.")
    print("A fáklyát megnézve, láttad, hogy el lehet mozdítani.")
    print("Elmozdítod és egy titkos ajtó nyílik ki a kőfalból.")
    print("Átmentél, a sírás egyre hangosabb lett.")
    print("Egy szobában találtad magad. Körbenézve láttál valamit.")
    print("A húgod volt, s csak sírt egymagában a szoba közepén.")
    print("Mikor közelebb léptél, felismert, majd sikítani kezdett.")
    print("Következő pillanatban annyit láttál, hogy egy golyó hasított át a fején.")
    print("OTT A GYILKOS! - Majd minden gondod elszállt, hirtelen szabad lettél.")
    time.sleep(23)
    print()
    print("Újra próbálod?")
    print()
    print("1 - Igen, megpróbálom mégegyszer!")
    print("2 - Inkább hányok, na csá!")
    a = valasztas(2)
    time.sleep(3)
    if a == 1:
        from Body import main, pontszam
        main(pontszam+1)
    elif a == 2:
        exit()

    
        

def igen_nem():
    b = input("")
    if b[0] == "I" or b[0] == "i" or b[1] == "g" or b[1] == "G":
        os.system('cls')
        print()
        print("Elkezded követni a hang írányát.")
        print("Éppen egy folyosón mész át, mikor az hírtelen végetért.")
        print("Körbenézel.")
        time.sleep(7)
        print("Nem találsz semmit, tovább keresgélsz?")
        print()
        print("1 - Vissza fordulok, mielőtt bárki is ideérne.")
        print("2 - Megnézem mégegyszer")
        a = valasztas(2)
        if a == 1:
            templom_elott()
        elif a == 2:
            siras()
    elif b[0] == "n" or b[0] == "N" or b[1] == "e" or b[1] == "E":
        templom_elott()
    else:
        print()
        print("Nem értem, próbáld újra.")
        igen_nem()

def loot():
    print()
    print("Mit csinálsz?")
    print()
    print("1 - Megnézem, van-e nála valami.")
    print("2 - Bemegyek a templomba.")
    print("3 - Elmenekülök, mielőtt bárki is észrevenné.")
    a = valasztas(3)
    if a == 1:
        os.system('cls')
        print("Egy névjegykártya volt nála.")
        print("Király Atilla. Az apád neve...")
        print()
        print(zold + '+ "Névjegykártya" hozzáadva a tárgyaidhoz' + RESET)
        targyak.append("Névjegykártya")
        print()
        print("Mit teszel?")
        print()
        print("1 - bemegyek a templomba.")
        print("2 - elmenekülök.")
        a = valasztas(2)
        if a == 1:
            os.system('cls')
            print("Bementél a templomba. A templom üresnek tűnt.")
            print("Tovább sétáltál szép lassan az oltárhoz.")
            print("Ott halk sírást hallottál.")
            print()
            print("Megnézed, hogy mi az? (Igen / Nem)")
            igen_nem()
        elif a == 2:
            menekul()
    elif a == 2:
        os.system('cls')
        print("Bementél a templomba. A templom üresnek tűnt.")
        print("Tovább sétáltál szép lassan az oltárhoz.")
        print("Ott halk sírást hallottál.")
        print()
        print("Megnézed, hogy mi az? (Igen / Nem)")
        igen_nem()
    elif a == 3:
        menekul()
        

def halal():
    print("A pap csak meredten bámul maga elé.")
    print("Szinte meg sem mozdul. Csak néz előre, miközben szemei beszürkűlnek.")
    print("Szép lassan kezével odanyúl az általad vétet seb helyére.")
    print("Miközben vérével teli kezét nézi, rádnéz, majd megszólal:")
    print()
    print("    Isten mindig megbocsált. Légy jó Fiam, s ne bánts másokat!")
    loot()
    

def leszur():
    os.system('cls')
    i = 0
    while i < len(targyak) and targyak[i] != "kés" and targyak[i] != "kard":
        i += 1
    if i < len(targyak):
        print(f"Leszúrtad a {targyak[i]} nevezetű tárgyaddal!")
        halal()
    elif i == len(targyak):
        print("Nincs nálad olyan tárgy, amivel megteheted. ):")
        time.sleep(3)
        os.system('cls')
        pap_valasztas(1, 0)
        

def beszed():
    os.system('cls')
    print("Gergely: Nem értem az életem értelmét!")
    print()
    print("Értem, Fiam. Tudod, az életnek az az értelme, amit mi adunk neki.")
    print("Eddig az volt az élet értelme, hogy túléljünk.")
    print("Így viszont, hogy már nem kell mindentől aggódnunk, elértünk egy szintet.")
    print('A "Szabadságot". De ezt rengeteg ember nem tudja helyesen kezelni.')
    print("Tehát szerintem az az élet értelme, hogy felfogod, hogy szabad vagy.")
    print("Találj magadnak egy értelmet!")
    time.sleep(10)
    print()
    i = 0
    while i < len(tulajdonsag) and tulajdonsag[i] != "karizma":
        i += 1
    if i == len(tulajdonsag):
        print(zold + "+ 1 karizma megszerezve!" + RESET)
        tulajdonsag.append("karizma")
    else:
        print("Bugot nem használunk ki. He-he.")
    pap_valasztas(1, 1)
    

def pap_2(a):
    if a == 1:
        beszed()
    elif a == 2:
        papsag()
    elif a == 3:
        otthagy()
    elif a == 4:
        leszur()
        
def pap_valasztas(a=0, b=0):
    print()
    print("Mit teszel?")
    print()
    if b == 0: 
        print('1 - "Nem értem az életem értelmét, segíts nekem."')
    print('2 - "beszeretnék állni szerzetesnek!"')
    print("3 - Meggondoltam magam, otthagyom.")
    if a == 0:
        print("4 - Leszúrom!")
    else:
        print("Nincs nálad megfelelő tárgy!")
    s = valasztas(4)
    print()
    if b == 1 and s == 1:
        os.system('cls')
        print("Óvatosan, nem szeretném, ha hibába ütköznénk.")
        print("Próbáld újra! (De, ne az 1-gyel.)")
        pap_valasztas(0, 1)
    pap_2(s)
    
    

def pap():
    os.system('cls')
    print("Életedben nem találtad az értelmet, Istenhez fordultál.")
    print("Letérdeltél, s egy papír hullott az öledbe.")
    print('A papíron egy "Papot keresünk!" felírat volt olvasható.')
    print("Ezt egy jelnek vetted és elindultál a templomhoz.")
    print("Mikor odaértél, egy pap fogadott téged.")
    print()
    print('    "Mi járatban errefelé Fiam?"   ') 
    pap_valasztas()
