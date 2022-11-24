# ----------- NALOGA 3 -----------
# Namestite knjižnico requests in spišite funkcijo, ki za iskalni niz vrne html kodo rtvslo 
# iskalnika novic (https://www.rtvslo.si/iskalnik?q=iskalni niz).

import requests

def pridobiHTML (povezava):
    iskanje = 'https://www.rtvslo.si/iskalnik?q=' + str(povezava)
    r = requests.get(iskanje)
    return r

iskalniNiz = input('vnesi iskalni niz: ')

print(pridobiHTML(iskalniNiz))

