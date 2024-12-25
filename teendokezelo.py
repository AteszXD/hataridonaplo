import json

# Betöltés
def betolt(username):
    with open(f"{username}.json", "r", encoding="utf-8") as userdb:
        return json.load(userdb)
    
# Módositás
def modositas(username, teendok):
    with open(f"{username}.json", "w", encoding="utf-8") as f:
        json.dump(teendok, f, default=str, indent=4)