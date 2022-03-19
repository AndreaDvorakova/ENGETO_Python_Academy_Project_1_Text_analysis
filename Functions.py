from Constants import *

cista_slova = []
slova_title = []
slova_upper = []
slova_lower = []
slova_cisla = []
slovnik = {}
i = 1
cislo_in = ''
volba = ''

def statistika_textu (cislo_in):
    list_slov = TEXTS[cislo_in].split()
    for slovo in list_slov:
        ciste_slovo = slovo.strip(',.-')
        cista_slova.append(ciste_slovo)

    for slovo in cista_slova:
        if slovo.istitle():
            slova_title.append(slovo)
        elif slovo.isalpha() and slovo.isupper():
            slova_upper.append(slovo)
        elif slovo.islower():
            slova_lower.append(slovo)
        elif slovo.isnumeric():
            slova_cisla.append(slovo)
    print('There are ', len(cista_slova), ' words in the selected text.')
    print('There are ', len(slova_title), ' titlecase words.')
    print('There are ', len(slova_upper), ' uppercase words.')
    print('There are ', len(slova_lower), ' lowercase words.')
    print('There are ', len(slova_cisla), ' numeric strings.')
    soucet_celkem = 0
    for cislo in slova_cisla:
        soucet_celkem = soucet_celkem + int(cislo)
    print('The sum of all the numbers ', soucet_celkem, '.')

def statistika_slov_graficky ():
    for slovo in cista_slova:
        l = len(slovo)
        slovnik[l] = slovnik.get(l, 0) + 1

