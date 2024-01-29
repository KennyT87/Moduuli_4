"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
"""
import random

luku = random.randint(1,10)
arvaus = int(input("Peli alkaa!\nArvaa kokonaisluku:\n"))

if luku == arvaus:
    print("Arvasit oikein!")

while True:
    if luku == arvaus:
        print("Oikein! Peli loppuu.")
        break
    if arvaus > luku:
        arvaus = int(input("Liian suuri arvaus!\nArvaa uudelleen:\n"))
    if arvaus < luku:
        arvaus = int(input("Liian pieni arvaus!\nArvaa uudelleen:\n"))