import time

# Uporabnika zaprosite naj vnese neko celo število. 
# To vrednost shranite v spremenljivko z imenom n in jo izpišite in izpišite njen tip. 
# Nato to vrednost pretvorite v float vrednost. 
# Dobljeno float vrednost shranite v spremenljivko n. 
# Nato n izpišite in izpišite njen tip.

n = input("Vnesite neko celo število")
print("OK, vnesli ste vrednost" + n + "ki je tipa: " + str(type(n)))

print("meljem", end = ' ')
time.sleep(0.3)
print(".", end = ' ')
time.sleep(0.3)
print(".", end = ' ')
time.sleep(0.3)
print(".", end = ' ')

n = float(n)
print("sedaj sem pretvoril vašo vneseno vrednost " + n + ", shranjeno v spremenljivki n v tip spremenljivke " + str(type(n)))