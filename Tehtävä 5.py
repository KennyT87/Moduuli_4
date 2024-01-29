"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
"""
tunnus = "python"
salasana = "rules"
kokeilut = 5

user_tunnus = input("Anna käyttäjätunnus: ")
user_salasana = input("Anna salasana: ")
while True:
    if kokeilut == 1:
        print("Pääsy evätty.")
        break
    if (user_tunnus != tunnus) or (user_salasana != salasana):
            print("Väärä tunnus tai salasana.")
            kokeilut -= 1
    user_tunnus = input("Anna käyttäjätunnus: ")
    user_salasana = input("Anna salasana: ")
    if (user_tunnus == tunnus) and (user_salasana == salasana):
        print("Tervetuloa!")
        break