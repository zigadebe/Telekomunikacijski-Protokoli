# Podobno kot v prvem primeru napišite funkcijo ki sprejme URL API-ja (vrača vrednosti v JSNO formatu) in vrnite vrednost kot slovar. 
# Še vedno izvedite validacijo.
import requests
import json

def get_api_data(url):
    koda = requests.get(url)
    if (koda.status_code == 200):
        return json.loads(koda.text)
    else:
        return False

# preizkusite na primerih
data = get_api_data("https://jsonplaceholder.typicode.com/todos/1")
print(data)

data = get_api_data("https://jsonplaceholder.typicode.com/nedala/nedala")
print(data)
