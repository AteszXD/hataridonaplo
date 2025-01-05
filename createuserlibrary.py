import os
import shutil # ez eredetileg az os helyett lett volna de nincs benne getsize()
import json

def konyvtarletrehozo(username): # Személyes könytár létrehozása

    if not os.path.exists("userek"):
        os.makedirs("userek")

    with open(f"{username}.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4) # Amig nincs teendő hozzáadva addig legyen egy üres lista
    
    shutil.move(f"{username}.json", f"userek/{username}.json")