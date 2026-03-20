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

Pokemon1 = Pokemon("Pflanze", "Tackle",8, "Rankenhieb",12,"Slam",15, "Bisasam",100)

Pokemon2 = Pokemon("Feuer", "Glut",10, "Fruststampfer",14,"Säuselstimme",10, "Krokel",100)

Pokemon3 = Pokemon("wasser","Blubbstrahl",16,"Klaps",8,"Aquaknarre",10,"Froxy",100)

Pokemon4 = Pokemon("Elektro","Eisenschweif",10,"Ruckzuckhieb",10,"Donnerblitz",12,"Pikachu",100)

Pokemon5 = Pokemon("Flug","Akrobatik",12,"Nitroladung",12,"Pikser",6,"Dartignis",100)

Pokemon6 = Pokemon("Kampf","Mogelhieb",6,"Fußtritt",10,"",12,"Machock",100)

Pokemon7 = Pokemon("Normal","",,"",,"",,"",100)

Pokemon8 = Pokemon("Gestein","",,"",,"",,"",)

Pokemon9 = Pokemon("Boden","",,"",,"",,"",)

Pokemon10 = Pokemon("Normal","",,"",,"",,"",)

Pokemon11 = Pokemon("Käfer","",,"",,"",,"",)

Pokemon12 = Pokemon("Psycho","",,"",,"",,"",)

Pokemon13 = Pokemon("Gift","",,"",,"",,"",)

Pokemon14 = Pokemon("Unlicht","",,"",,"",,"",)

Pokemon15 = Pokemon("Fee","",,"",,"",,"",)

Pokemon16 = Pokemon("Drache","",,"",,"",,"",)

Pokemon17 = Pokemon("Stahl","",,"",,"",,"",)

Pokemon18 = Pokemon("Eis","",,"",,"",,"",)

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







































































































































































































































































































































































































































































































































