import json

with open("arangodb.txt") as f:
    db = json.load(f)
    with open ("aradb.json", "w") as f:
        json.dump(db, f)
