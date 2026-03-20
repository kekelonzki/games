class Pokemon:
    def __init__(self, typ, attacke1, attacke2, name):
        self.typ = typ
        self.attacke1 = attacke1
        self.attacke2 = attacke2
        self.name = name

Pokemon1 = Pokemon("Pflanze", "Blattwerk", "Rankenhieb", "Bisasam")
Pokemon2 = Pokemon("Feuer", "Glut", "Feuerschlag", "Krokel")

print("Ein wildes " + Pokemon1.name + " greift dich an")
print("Du setzt " + Pokemon2.name + " ein, was soll " + Pokemon2.name + " tun, " + Pokemon2.attacke1 + " oder " + Pokemon2.attacke2 + "?")

answer = input().strip().lower()  # Benutzereingabe in Kleinbuchstaben umwandeln und Leerzeichen entfernen

if answer == Pokemon2.attacke1.lower():
    print(Pokemon2.name + " setzt " + Pokemon2.attacke1 + " ein, die Attacke ist sehr effektiv")
elif answer == Pokemon2.attacke2.lower():
    print(Pokemon2.name + " setzt " + Pokemon2.attacke2 + " ein, die Attacke ist sehr effektiv")
else:
    print("Ungültige Eingabe")