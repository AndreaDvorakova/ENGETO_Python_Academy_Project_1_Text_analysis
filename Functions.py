from Constants import *

cista_slova = []
slova_title = []
slova_upper = []
slova_lower = []
slova_cisla = []
suma_celkem = 0


list_slov = TEXTS[0].split()
for slovo in list_slov:
    ciste_slovo = slovo.strip(',.')
    cista_slova.append(ciste_slovo)

for slovo in list_slov:
    if slovo.istitle():
        slova_title.append(slovo)
    elif slovo.isalpha() and slovo.isupper():
        slova_upper.append(slovo)
    elif slovo.islower():
        slova_lower.append(slovo)
    elif slovo.isnumeric():
        slova_cisla.append(slovo)

for cislo in slova_cisla:
    suma_celkem = suma_celkem + int(cislo)

pocet_slov = len(cista_slova)
pocet_slova_title = len(slova_title)
pocet_slova_upper = len(slova_upper)
pocet_slova_lower = len(slova_lower)
pocet_slova_cisla = len(slova_cisla)