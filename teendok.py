import datetime
import teendokezelo
import user
import json

teendok = []

def fomenu():
    while True:
        print("\n=== Határidőnapló ===")
        print("1. Teendő hozzáadása")
        print("2. Teendők megtenkitése")
        print("3. Teendő módosítása")
        print("4. Aktuális hét feladatai")
        print("5. Teendő törlése")
        print("6. Sürgős feladatok")
        print("7. Kijelentkezés")

        muvelet = input("Válassza ki a műveletet: ")

        if muvelet == "1":
            teendo_add()
        elif muvelet == "2":
            teendok_megt2()
        elif muvelet == "3":
            teendo_modosit()
        elif muvelet == "4":
            aktualis_het()
        elif muvelet == "5":
            teendo_torlese()
        elif muvelet == "6":
            surgos()
        elif muvelet == "7":
            print("Sikeres kijelentkezés. Viszontlátásra!")
            break
        else:
            print("Helytelen szám.")

def teendo_add():
    teendo_hozz = input("Adja meg a teendő leírását: ")

    while True:
        hatar = input("Adja meg a teendő határidejét (ÉÉÉÉ-HH-NN): ")
        try:
            teendo_hatar = datetime.datetime.strptime(hatar, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Érvénytelen dátum.")

    
    statusz = input("Adja meg a státuszt (függőben/kész): ").lower()
    while statusz != "függőben" and statusz != "kész":
        statusz = input("Adja meg a státuszt (függőben/kész): ").lower()

    teendo = {
        'leírás': teendo_hozz,
        'határidő': teendo_hatar,
        'státusz': statusz
    }
    
    teendok.append(teendo)
    teendokezelo.hozzaadas(user.user, teendo)
    print("Teendő sikeresen hozzáadva.")

def teendok_megt2():
    username = user.user
    with open(f"userek/{username}.json", "r", encoding="utf-8") as f:
        teendokfile = json.load(f)
    
    mai_nap = datetime.date.today()
    ervenyes_teendok = [
        teendo for teendo in teendokfile 
        if datetime.datetime.strptime(teendo['határidő'], "%Y-%m-%d").date() >= mai_nap and teendo['státusz'] != "kész"
    ]

    if ervenyes_teendok:
        print("\nElvégzendő teendők:")
        for i, teendo in enumerate(ervenyes_teendok, 1):
            print(f"{i}. {teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")
    else:
        print("Nincs teendő.")

def teendok_megt():
    username = user.user
    with open(f"userek/{username}.json", "r", encoding="utf-8") as f:
        teendokfile = json.load(f)
        
    if len(teendokfile) > 0:
        print("\nÖsszes teendő:")
        for i, teendo in enumerate(teendokfile, 1):
            print(f"{i}. {teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")
    else:
        print("Nincs teendő.")

def teendo_modosit():
    teendok_megt()
    username = user.user
    with open(f"userek/{username}.json", "r", encoding="utf-8") as f:
        teendokfile = json.load(f)
    try:
        teendo_id = int(input("Adja meg a teendő számát: "))
        if teendo_id < 1 or teendo_id > len(teendokfile):
            print("Helytelen szám.")
            return
    except ValueError:
        print("Kérem próbáljon egy másik számot.")
        return

    teendo_hozz = input("Adja meg a teendő leírását: ")
    while True:
        hatar = input("Adja meg a teendő határidejét (ÉÉÉÉ-HH-NN): ")
        try:
            teendo_hatar = datetime.datetime.strptime(hatar, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Érvénytelen dátum.")

    statusz = input("Adja meg a státuszt (függőben/kész): ").lower()
    while statusz != "függőben" and statusz != "kész":
        statusz = input("Adja meg a státuszt (függőben/kész): ").lower()

    teendo = {
        'leírás': teendo_hozz,
        'határidő': teendo_hatar,
        'státusz': statusz
    }
    
    teendokfile[teendo_id - 1] = teendo
    with open(f"userek/{username}.json", "w", encoding="utf-8") as f:
            json.dump(teendokfile, f, ensure_ascii=False, indent=4, default=str)

    print("Teendő frissítve.")

def aktualis_het():
    username = user.user
    with open(f"userek/{username}.json", "r", encoding="utf-8") as f:
        teendokfile = json.load(f)
    mai_nap = datetime.date.today()
    het = mai_nap + datetime.timedelta(days=(6 - mai_nap.weekday()))  
    
    heti_teendok = [teendo for teendo in teendokfile if mai_nap <= datetime.datetime.strptime(teendo['határidő'], "%Y-%m-%d").date() <= het]

    if not heti_teendok:
        print("Nincs teendő ezen a héten.")
    else:
        print("\nE heti teendők:")
        for i, teendo in enumerate(heti_teendok, 1):
            print(f"{i}. {teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")

def teendo_torlese():
    teendok_megt()
    username = user.user
    with open(f"userek/{username}.json", "r", encoding="utf-8") as f:
        teendokfile = json.load(f)
    try:
        teendo_id = int(input("Adja meg a törölni kívánt teendő számát: "))
        if teendo_id < 1 or teendo_id > len(teendokfile):
            print("Helytelen szám.")
            return
    except ValueError:
        print("Kérem próbáljon egy másik számot.")
        return

    del teendokfile[teendo_id - 1]
    with open(f"userek/{username}.json", "w", encoding="utf-8") as f:
        json.dump(teendokfile, f, ensure_ascii=False, indent=4, default=str)

    print("Teendő törölve.")

def surgos():
    username = user.user
    with open(f"userek/{username}.json", "r", encoding="utf-8") as f:
        teendokfile = json.load(f)
    
        mai_nap = datetime.date.today()
    surgosseg = {
        "halaszthatatlan": [],
        "surgos": [],
        "kevesbe_surgos": [],
        "nem_surgos": []
    }

    for teendo in teendokfile:
        hatarido = datetime.datetime.strptime(teendo['határidő'], "%Y-%m-%d").date()
        statusz = teendo['státusz']
        kulonbseg = (hatarido - mai_nap).days

        if hatarido >= mai_nap and statusz != "kész":
            if kulonbseg <= 1: 
                surgosseg["halaszthatatlan"].append(teendo)
            elif 2 <= kulonbseg <= 3:
                surgosseg["surgos"].append(teendo)
            elif 4 <= kulonbseg <= 7:
                surgosseg["kevesbe_surgos"].append(teendo)
            elif kulonbseg > 7:
                surgosseg["nem_surgos"].append(teendo)

    if any(surgosseg.values()):
        if surgosseg["halaszthatatlan"]:
            print("---HALASZTHATATLAN---")
            for teendo in surgosseg["halaszthatatlan"]:
                print(f"{teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")

        if surgosseg["surgos"]:
            print("\n---Sürgős---")
            for teendo in surgosseg["surgos"]:
                print(f"{teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")

        if surgosseg["kevesbe_surgos"]:
            print("\n---Kevésbé sürgős---")
            for teendo in surgosseg["kevesbe_surgos"]:
                print(f"{teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")

        if surgosseg["nem_surgos"]:
            print("\n---Nem sürgős---")
            for teendo in surgosseg["nem_surgos"]:
                print(f"{teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")
    else:
        print("Nincsenek teendők.")

       
if __name__ == "__main__":
    fomenu()