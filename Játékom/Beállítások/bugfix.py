from random import randrange
import time
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

