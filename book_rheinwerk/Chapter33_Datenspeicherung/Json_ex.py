""" JSON Example
page 614

Author: Oliver Zott
Date: 2019-11-11
"""

import json

# entry definition
eintrag = {
    "Vorname": "Donald",
    "Nachname": "Duck",
    "Adresse": ["Erpelweg", 12, 12345, "Entenhausen"],
    "Alter": 81
}

# Create json object on the fly
s = json.dumps(eintrag)
print(s)

# Read json onjects on the fly
print(json.loads(s)['Ausgabe'])

# Create json file
with open("eintrag.json", "w") as f:
    json.dump(eintrag, f)

# read json file
print()
print("Load JSON file: ")
with open("eintrag.json", "r") as f:
    print(json.load(f))


