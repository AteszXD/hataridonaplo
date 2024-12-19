import os

eleresiut = "userek.txt" # Ez a fájl akár ÜRESEN is kell!!!
sikereslogin = False

while sikereslogin == False:
    if os.path.getsize(eleresiut) == 0: # Regisztráció
        print("Még nem létezik felhasználó, kérem hozzon létre egyet!")
        username = input("Kérem adjon meg egy felhasználónevet: ")
        password = input("Kérem adjon meg egy jelszót: ")
        f = open(f"userek.txt", "a")
        f.write(f"{username};{password}")
        f.close()
        sikereslogin = True
# Ezt még ki kell dolgozni
# else:
#     print("Kérem jelentkezzen be!")
#     username = input("Kérem adja meg a felhasználónevet: ")
#     password = input("Kérem adja meg a jelszót: ")




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