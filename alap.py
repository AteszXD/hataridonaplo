import os # os.path.getsize(elérési_út) megnézi az adott elérési úton található fájl méretét, mivel a rootban van a fájl így ide csak a fájl neve kellett
import createuserlibrary
import teendok
import teendokezelo
import user

sikereslogin = False
eleresiut = "userek.txt"

if not os.path.exists(eleresiut):
    f = open(eleresiut, "x")
    f.close()

# Bejelentkezés/Regisztráció

while sikereslogin == False:

    if os.path.getsize(eleresiut) == 0: # Regisztráció, ha üres fájl
        print("Még nem létezik felhasználó, kérem hozzon létre egyet!")
        username = input("Kérem adjon meg egy felhasználónevet: ")
        password = input("Kérem adjon meg egy jelszót: ")

        with open(eleresiut, "a", encoding="utf-8") as f:
            f.write(f"{username};{password}\n")

        print("Köszönjük a regisztrációt!")
        createuserlibrary.konyvtarletrehozo(username)

        sikereslogin = True
        user.user = username

    else: # Login, ha van user
        print("Kérem jelentkezzen be!")
        username = input("Kérem adja meg a felhasználónevet: ")
        password = input("Kérem adja meg a jelszót: ")

        beirtadat = f"{username};{password}"
        with open(eleresiut, "r", encoding="utf-8") as adatbazis:
            sorok = adatbazis.readlines()

            for sor in sorok:

                if sor.strip() == beirtadat:
                    print(f"Sikeres bejelentkezés, üdvözöljük {username}!")
                    sikereslogin = True
                    user.user = username
                    teendokezelo.betolt(f"userek/{username}.json")
                else:
                    print("Helytelen felhasználónév, vagy jelszó. Próbálja Újra!")

# Teendők
teendok.fomenu()



"""
with open ('userek.txt','r',encoding='utf-8') as felhasznalok:

    for user in felhasznalok:
        felhasznalo = user.strip().split(';')
        useradatok = {'username': felhasznalo[0], 'password': felhasznalo[1]}
        userek.append(user)
print(userek)


# A saját adatbázis létrehozása
f = open(f"{useradatok(felhasznalo[0])}.txt", "a")
f.write("1234")
f.close()
"""

# felhasznalo[x] (pl. Bözsi) adati saját .json fájlba lesznek tárolva, pl. Bözsi.json