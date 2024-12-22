import os
import shutil # ez eredetileg az os helyett lett volna de nincs benne getsize()

def konyvtarletrehozo(username): # Személyes könytár létrehozása
    with open(f"{username}.txt", "a", encoding="utf-8") as f:
        f.write("Ide majd maga a határidő jön, majd változóként")
    if not os.path.exists("userek"):
        os.makedirs("userek")
    shutil.move(f"{username}.txt", "userek/"f"{username}.txt")