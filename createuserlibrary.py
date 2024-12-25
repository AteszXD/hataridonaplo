import os
import shutil # ez eredetileg az os helyett lett volna de nincs benne getsize()

def konyvtarletrehozo(username): # Személyes könytár létrehozása
    with open(f"{username}.json", "a", encoding="utf-8") as f:
        f.write("Ide majd maga a határidő jön, majd változóként")
    if not os.path.exists("userek"):
        os.makedirs("userek")
    shutil.move(f"{username}.json", "userek/"f"{username}.json")