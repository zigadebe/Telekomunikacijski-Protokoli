# ----------- NALOGA 4 -----------
# Poiščite vsa praštevila med 1 in 50.

from turtle import st


def ali_prastevilo(stevilo):
    if stevilo > 1:
        for i in range(2, int(stevilo/2)+1):
            if (stevilo % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0

for stevilo_za_preverit in range(0, 50):
    if (ali_prastevilo(stevilo_za_preverit)):
        print(stevilo_za_preverit)
            
# -------------------------------