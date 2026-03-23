import random as rd
class Pokemon:
    def __init__(self, typ, atk1,dmg1, atk2,dmg2, atk3,dmg3, name,kp):
        self.typ =  typ
        self.atk1 = atk1
        self.atk2 = atk2
        self.atk3 = atk3
        self.name = name
        self.kp = kp
        self.dmg1 = dmg1
        self.dmg2 = dmg2
        self.dmg3 = dmg3

atk ={"Pflanze":["Blattwerk" , "Rankenhieb"],
    "Feuer": ["Glut","Nitroladung"],
    "Wasser":["Blubbstrahl","aquaknarre"],
    "Elektro":["Donnerblitz"],
    "Flug":["Luftschnitt","Akrobatik","Pikser"],
    "Kampf":["Kreuzhieb","Fußtritt"],
    "Normal":["sternenschauer","Klaps","Tackle","Ruckzuckhieb","Slam","Triplette","Mogelhieb","Schlitzer"],
    "Gestein":["Juwelen kraft","Steinkante","Steinhagel"],
    "Boden":["Fruststampfer","Dampfwalze","Schaufler"],
    "Geist":[],
    "Käfer":[],
    "Psycho":[],
    "Gift":[],
    "Unlicht":[],
    "Fee":[],
    "Drache":[],
    "Stahl":[],
    "Eis":[],
    

Pokemon1 = Pokemon("Pflanze", "Blattwerk",10, "Rankenhieb",12,"Slam",14, "Bisasam",100)

Pokemon2 = Pokemon("Feuer", "Glut",10, "Fruststampfer",14,"Säuselstimme",10, "Krokel",100)

Pokemon3 = Pokemon("Wasser","Blubbstrahl",16,"Klaps",8,"Aquaknarre",10,"Froxy",100)

Pokemon4 = Pokemon("Elektro","Eisenschweif",12,"Ruckzuckhieb",10,"Donnerblitz",14,"Pikachu",100)

Pokemon5 = Pokemon("Flug","Akrobatik",12,"Nitroladung",12,"Pikser",6,"Dartignis",100)

Pokemon6 = Pokemon("Kampf","Mogelhieb",6,"Fußtritt",10,"kreuzhieb",12,"Machock",100)

Pokemon7 = Pokemon("Normal","sternenschauer",10,"Tackle",8,"Triplette",12,"Porygon",100)

Pokemon8 = Pokemon("Gestein","Steinhagel",12,"Steinkante",12,"Slam",14,"Onix",110)

Pokemon9 = Pokemon("Boden","Schaufler",10,"Juwelen kraft",10,"dampfwalze",14,"Kaumalat",)

Pokemon10 = Pokemon("Geist","Spukball",14,"Biss",12,"Juwelen kraft",10,"Zobiris",100)

Pokemon11 = Pokemon("Käfer","Attack Befehl",12,"Heilungs Befehl",10,"Käfergebrumm",10,"Honweisel",100)

Pokemon12 = Pokemon("Psycho","Psychoshock",14,"Telekinese",12,"Sternenschauer",10,"Psiaugon",100)

Pokemon13 = Pokemon("Gift","Schlammwoge",12,"Gifthieb",14,"Ruckzuckhieb",10,"Affiti",100)

Pokemon14 = Pokemon("Unlicht","Finsteraura",12,"Neck Strike",14,"Tackle",8,"Galar Geradaks",100)

Pokemon15 = Pokemon("Fee","Diebes Kuss",8,"Luftschnitt",12,"Feenbrise",12,"Togekiss",100)

Pokemon16 = Pokemon("Drache","Draco Meteor",16,"Drachen klaue",14,"slam",14,"Brutalanda",110)

Pokemon17 = Pokemon("Stahl","Kopfnuss",12,"Licht kanone",14,"Erdkräfte",14,"Schilterus",110)

Pokemon18 = Pokemon("Eis","Blizzard",14,"Eis strahl",14,"Schlitzer",12,"Glaziola",100)

print ("Ein wildes " + Pokemon1.name + " greift dich an")
print ("Du setzt " + Pokemon2.name + " ein, was soll " + Pokemon2.name + " tun, " + Pokemon2.atk1 + " oder " + Pokemon2.atk2 + "?")

counter1 = Pokemon1.kp
counter2 = Pokemon2.kp

while 1:
    answer = input().strip().capitalize()
    if answer == Pokemon2.atk1:
        print(Pokemon2.name + " setzt " + Pokemon2.atk1 + " ein, die attacke ist  sehr effektiv")
        counter1 -= (Pokemon2.dmg1 * 1.5)
        print(Pokemon1.name + " hat " + str(int(counter1)) + " kp")
    elif answer == Pokemon2.atk2:
        print(Pokemon2.name + " setzt " + Pokemon2.atk2 + " ein")
        counter1 -= Pokemon2.dmg2
        print(Pokemon1.name + " hat " + str(int(counter1)) + " kp")
    else:
        print("Bisasam benutzt das KAME HAME HA um dir zu zeigen das du wohl eine ungültige eingabe benutzt hast")

    if counter1 <= 0:
        print ("Du gewinnst")
        break

    zufahls_attacke=rd.randint(1,2)
    if zufahls_attacke == 1:
        print("Bisasam setzt " + Pokemon1.atk1 + " ein")
        counter2 -=  Pokemon1.dmg1
        print(Pokemon2.name + " hat " + str(int(counter2)) + " kp")
    elif zufahls_attacke == 2:
        print("Bisasam setzt " + Pokemon1.atk2 + " ein, die attacke ist nicht sehr effektiv")
        counter2 -= (Pokemon1.dmg2 / 2)
        print(Pokemon2.name + " hat " + str(int(counter2)) + " kp")

    elif counter2 <= 0:
        print ("Wie.... einfach nur wie.... WIE HAST DU VERLOREN????????")
        break







































































































































































































































































































































































































































































































































