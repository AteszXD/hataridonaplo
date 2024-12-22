import os # os.path.getsize(elérési_út) megnézi az adott elérési úton található fájl méretét, mivel a rootban van a fájl így ide csak a fájl neve kellett
import createuserlibrary

eleresiut = "userek.txt" # Ez a fájl akár üresen is kell!!!
sikereslogin = False

while sikereslogin == False:
    if os.path.getsize(eleresiut) == 0: # Regisztráció, ha üres fájl
        print("Még nem létezik felhasználó, kérem hozzon létre egyet!")
        username = input("Kérem adjon meg egy felhasználónevet: ")
        password = input("Kérem adjon meg egy jelszót: ")
        with open(eleresiut, "a") as f:
            f.write(f"{username};{password}\n")
        print("Köszönjük a regisztrációt!")
        createuserlibrary.konyvtarletrehozo(username)
        sikereslogin = True
    elif os.path.getsize(eleresiut) != 0: # Login, ha van user
        print("Kérem jelentkezzen be!")
        username = input("Kérem adja meg a felhasználónevet: ")
        password = input("Kérem adja meg a jelszót: ")
        beirtadat = f"{username};{password}"
        with open(eleresiut, "r") as adatbazis:
            sorok = adatbazis.readlines()
            for sor in sorok:
                if sor.strip() == beirtadat:
                    print(f"Sikeres bejelentkezés, üdvözöljük {username}!")
                    sikereslogin = True
                else:
                    print("Helytelen felhasználónév, vagy jelszó. Próbálja Újra!")




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

# felhasznalo[x] (pl. Bözsi) adati saját .txt fájlba lesznek tárolva, pl. Bözsi.txt