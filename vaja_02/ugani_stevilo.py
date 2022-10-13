import random

neznano = random.randrange(0,30)
print("Ugani število med 0 in 30.")

def preveri(st):
    if st < 0:
        print("Vnesi stevilo vecje od 0.")
        return 0
    elif st > 30:
        print("Vnesi stevilo manjse od 30.")
        return 0
    else:
        if st == neznano:
            print("Cestitam, uganil si stevilo")
            return 1
        else:
            print("poizkusi se enkrat")
            return 0

poskus = 5
rezulutat = 0
while poskus > 0:
    stevilo = int(input("Vnesi stevilo: "))
    rezultat = preveri(stevilo)
    if rezultat == 1:
        poskus = 0
    poskus -= 1

if rezultat == 0:
    print("Zmanjkalo ti je poskusov. Pravo stevilo je bilo " + str(neznano))
else:
    print("konec. Pravo stevilo je bilo " + str(neznano))


