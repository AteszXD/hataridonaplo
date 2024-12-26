import json

# Betöltés
def betolt(username):
    with open(f"userek/{username}.json", "r", encoding="utf-8") as userdb:
        return json.load(userdb)
    
# Hozzáadás
def hozzaadas(username, teendo):
    fajl = f"userek/{username}.json"

    with open(fajl, "r", encoding="utf-8") as f:
        jelenadat = json.load(f) # Ha nem kaptunk errort mert volt mit beolvasni akkor olvasd már be légy olyan kedves

    jelenadat.append(teendo) # Ez mindig egy nagy változó az össes teendővel ugyanis a .json-be csak egy lista lehet, mig az eddigi megoldás minden sessionben egy újat hozott létre

    with open(fajl, "w", encoding="utf-8") as f:
        json.dump(jelenadat, f, ensure_ascii=False, indent=4, default=str)