# ----------- NALOGA 2 -----------
#Uporabite knjižnico math in za spišite funkcijo, ki za poljubno polje števil vrne:
# - najmanjši element,
# - največji element
# - povprečje in
# - element polja, ki je najbližje povrečju.

import math

def najdiNajmanjsega(polje):
    najmanjsi = min(polje)
    return najmanjsi

def najdiNajvecjega(polje):
    najvecji = max(polje)
    return najvecji

def povprecje(polje):
    povprecjePolja = sum(polje) / len(polje)
    return povprecjePolja

def najdinajblizjega(polje):
    povprecjePolja = povprecje(polje)
    najblizji = polje[0]
    for i in range (1, len(polje)):
        if (abs(povprecjePolja - polje[i]) < abs(povprecjePolja - najblizji)):
            najblizji = polje[i]
    return najblizji

testnoPolje = [0, 4, 54, -33, 500, 323, 900, 342, 589, 611, -2, 4243, 33, 600]

print("------------------------------------------------------------------------------")
print("- testno polje: " + str(testnoPolje))
print("-")
print("- Najmanjsi element v testnem polju je: " + str(najdiNajmanjsega(testnoPolje)))
print("- Najvecji element v testnem polju je: " + str(najdiNajvecjega(testnoPolje)))
print("- Povprecje vseh elementov v testnem polju je: " + str(povprecje(testnoPolje)))
print("- Element najblizji povprecju je: " + str(najdinajblizjega(testnoPolje)))
print("------------------------------------------------------------------------------")