# ----------- NALOGA  -----------
# Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število. 
# Funkcija naj nato izpiše koliko let je uporabnik star (upoštevamo samo letnico rojstva) in vrne število let (celoštevilska vrednost). 
# EMŠO ima 14 številk XXXXyyyXXXXXXX. 5.,6.,7. številka predstavljajo letnico rojstva (999 -> 1999 leto rojstva).



def emso_leta_preracun():
    emso = input('Vnesi svoj EMSO: ')
    leto = ''

    for i in range(4,7):
        leto = leto + emso[i]
    
    leto = int(leto)

    leto = leto + 2000

    print(str(leto))

# primer uporabe 1
#starost = emso_leta_preracun()

emso_leta_preracun()
# -------------------------------