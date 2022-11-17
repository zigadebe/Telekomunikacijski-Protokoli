# ----------- NALOGA  -----------
# Napišite funkcijo, ki sprejme nabor podatkov v obliki dictionary-ja data in vrne največjo vrednost vsakega ključa (vrednosti so v obliki lista).

data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463],
       "hisa": [5346712, 9805, 16405, 137, 61463]}

najvecji = 0
tabela_najvecjih = []

def najvecja_vrednost(podatki): 
    for key in podatki:
        tabela = podatki[key]

        najvecji = tabela[0]
        for element in tabela:
            if (element > najvecji):
                najvecji = element
        
        tabela_najvecjih.append(najvecji)
    
    return tabela_najvecjih
        

        
# uporaba
vrednosti = najvecja_vrednost(data)
print(vrednosti)

# -------------------------------