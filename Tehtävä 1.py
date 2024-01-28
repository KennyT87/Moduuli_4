"""
Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
"""
nro = 1

while (nro <= 1000):
    if (nro % 3 == 0):
        print(nro)
    nro += 1