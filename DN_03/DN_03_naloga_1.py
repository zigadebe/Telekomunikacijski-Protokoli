# ----------- NALOGA  -----------
# Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število. 
# Funkcija naj nato izpiše koliko let je uporabnik star (upoštevamo samo letnico rojstva) in vrne število let (celoštevilska vrednost). 
# EMŠO ima 14 številk XXXXyyyXXXXXXX. 5.,6.,7. številka predstavljajo letnico rojstva (999 -> 1999 leto rojstva).

from datetime import date

def emso_leta_preracun():
    emso = input('Vnesi svoj EMSO: ')
    leto = ''
    tisocletje = 2000

    for i in range(4,7):
        leto = leto + emso[i]
    
    if (int(emso[4]) == 9):
        tisocletje = 1000
    elif (int(emso[4]) == 9):
        tisocletje = 1000
    
    print(emso[4])
    print(tisocletje)
    
    leto = int(leto)
    letorojstva = leto + tisocletje

    # Textual month, day and year
    today = date.today()	
    trenutnoLeto = int(today.strftime("%Y"))


    starost = trenutnoLeto - letorojstva
    return starost

# primer uporabe 1
starost = emso_leta_preracun()
print("Vaša starost je " + str(starost) + " let.")
# -------------------------------