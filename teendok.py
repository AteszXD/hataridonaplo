import datetime
import teendokezelo
import user

teendok = []

def fomenu():
    while True:
        print("\n=== Határidőnapló ===")
        print("1. Teendő hozzáadása")
        print("2. Összes teendő megtekintése")
        print("3. Teendő módosítása")
        print("4. Aktuális hét feladatai")
        print("5. Teendő törlése")
        print("6. Kijelentkezés")

        muvelet = input("Válassza ki a műveletet: ")

        if muvelet == "1":
            teendo_add()
        elif muvelet == "2":
            teendok_megt()
        elif muvelet == "3":
            teendo_modosit()
        elif muvelet == "4":
            aktualis_het()
        elif muvelet == "5":
            teendo_torlese()
        elif muvelet == "6":
            print("Sikeres kijelentkezés. Viszontlátásra!")
            break
        else:
            print("Helytelen szám.")

def teendo_add():
    teendo_hozz = input("Adja meg a teendő leírását: ")
    hatar = input("Adja meg a teendő határidejét (ÉÉÉÉ-HH-NN): ")
    try:
        teendo_hatar = datetime.datetime.strptime(hatar, "%Y-%m-%d").date()
    except ValueError:
        print("Érvénytelen dátumformátum. Kérjük, használja a ÉÉÉÉ-HH-NN formátumot.")
        return

    statusz = input("Adja meg a státuszt (függőben/kész): ").lower()

    teendo = {
        'leírás': teendo_hozz,
        'határidő': teendo_hatar,
        'státusz': statusz
    }
    
    teendok.append(teendo)
    teendokezelo.hozzaadas(user.user, teendo)
    print("Teendő sikeresen hozzáadva.")

def teendok_megt():
    if not teendok:
        print("Nincs teendő felírva.")
        return

    print("\nÖsszes teendők:")
    for i, teendo in enumerate(teendok, 1):
        print(f"{i}. {teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")


def teendo_modosit():
    teendok_megt()
    try:
        teendo_id = int(input("Adja meg a teendő számát: "))
        if teendo_id < 1 or teendo_id > len(teendok):
            print("Helytelen szám.")
            return
    except ValueError:
        print("Kérem próbáljon egy másik számot.")
        return

    uj_statusz = input("Adja meg a státuszt (függőben/kész): ").lower()
    teendok[teendo_id - 1]['státusz'] = uj_statusz
    print("Teendő státusz frissítve.")

def aktualis_het():
    mai_nap = datetime.date.today()
    het = mai_nap + datetime.timedelta(days=(6 - mai_nap.weekday()))  
    
    heti_teendok = [teendo for teendo in teendok if mai_nap <= teendo['határidő'] <= het]

    if not heti_teendok:
        print("Nincs teendő ezen a héten.")
    else:
        print("\nE heti teendők:")
        for i, teendo in enumerate(heti_teendok, 1):
            print(f"{i}. {teendo['leírás']} | Határidő: {teendo['határidő']} | Státusz: {teendo['státusz']}")


def teendo_torlese():
    teendok_megt()
    try:
        teendo_id = int(input("Adja meg a törölni kívánt teendő számát: "))
        if teendo_id < 1 or teendo_id > len(teendok):
            print("Helytelen szám.")
            return
    except ValueError:
        print("Kérem próbáljon egy másik számot.")
        return

    del teendok[teendo_id - 1]
    print("Teendő törölve.")

if __name__ == "__main__":
    fomenu()