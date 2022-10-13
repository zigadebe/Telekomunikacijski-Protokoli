# Uporabnika vprašajte za 3 celoštevilske vrednosti in jih izpišite s pomočjo print() in type(). 
# V eni vrstici preverite ali je druga vrednost enaka prvi in ali je tretja vrednost manjša ali enaka prvi.

print("")
print("")
print("------------------ DOMACA NALOGA 3 ------------------")
print("-")
a = int(input("- Vnesite prvo celo stevilo, A: "))
b = int(input("- Vnesite drugo celo stevilo, B: "))
c = int(input("- Vnesite drugo celo stevilo, C: "))
print("-")
print("- Ali velja, da je B == A in C <= A?")
odgovor = ((a == b) and (c <= a))
if (odgovor == True):
    print("- DA.")
else:
    print("- NE.")
print("---------------------------------------------------------")