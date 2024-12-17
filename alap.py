userek = []
with open ('userek.txt','r',encoding='utf-8') as felhasznalok:
    for user in felhasznalok:
        felhasznalo = user.strip().split(';')
        useradatok = {'username': felhasznalo[0], 'password': felhasznalo[1]}
        userek.append(user)
print(userek)

# felhasznalo[x] (pl. Bözsi) adati saját .txt fájlba lesznek tárolva, pl. Bözsi.txt