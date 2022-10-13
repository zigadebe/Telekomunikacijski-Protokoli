import time

# Uporabnika zaprosite naj vnese neko celo število. 
# To vrednost shranite v spremenljivko z imenom n in jo izpišite in izpišite njen tip. 
# Nato to vrednost pretvorite v float vrednost. 
# Dobljeno float vrednost shranite v spremenljivko n. 
# Nato n izpišite in izpišite njen tip.

n = input("Vnesite neko celo število:  ")
print("OK, vnesli ste vrednost " + str(n) + ", ki je shranjena v spremenljivki n, n je tipa: " + str(type(n)))

time.sleep(1)
print("")
print("")

n = float(n)
print("sedaj sem pretvoril vašo vneseno vrednost " + str(n) + ", shranjeno v spremenljivki n v tip spremenljivke " + str(type(n)))