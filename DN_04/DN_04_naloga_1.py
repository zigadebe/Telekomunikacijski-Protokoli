# ----------- NALOGA 1 -----------
#Z pomočjo knjižnice json pretvorite spodnji slovar podatki v JSON besedilo.

import json

podatki = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

besedilo = json.dumps(podatki)

print(besedilo)
