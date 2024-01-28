"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""
sentit = 0
while sentit >= 0:
    sentit = 2.54 * (float((input("Anna tuumat:\n"))))
    if sentit < 0:
        break
    print(f"Se on {sentit} senttiä.")