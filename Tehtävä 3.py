"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
import math

pienin = float(+math.inf)
suurin = float(-math.inf)

while True:
    lukuX = input("Anna luku (Enter lopettaa ohjelman):\n")
    if lukuX == "":
        print("Ohjelma loppuu.")
        break
    if lukuX != "":
        luku = float(lukuX)
        if luku <= pienin:
            pienin = luku
        if luku >= suurin:
            suurin = luku
if pienin != suurin and (pienin != float(+math.inf) and suurin != float(-math.inf)):
    print(f"Pienin luku on {pienin} ja suurin on {suurin}")
elif pienin == suurin:
    print(f"Luvut omat samat.")
else:
    print("Et antanut lukuja.")