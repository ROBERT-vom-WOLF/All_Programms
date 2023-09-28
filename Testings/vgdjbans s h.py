import random
game = 1
kartenfarben = ["Schippe", "Herz", "Blatt", "Raute"]

random_karte = random.randint(1, 13)
random_farbe = random.choices(kartenfarben, weights=[1, 1, 1, 1], k=1)


input("Enter, um eine karte zu ziehen")

while game == 1:
    if random_karte == 1 and random_farbe == "Schippe":
        print("Schippen Ass")
    if random_karte == 2 and random_farbe == "Schippe":
        print("Schippen 2")
    if random_karte == 3 and random_farbe == "Schippe":
        print("Schippen 3")
    if random_karte == 4 and random_farbe == "Schippe":
        print("Schippen 4")
    if random_karte == 5 and random_farbe == "Schippe":
        print("Schippen 5")
    if random_karte == 6 and random_farbe == "Schippe":
        print("Schippen 6")
    if random_karte == 7 and random_farbe == "Schippe":
        print("Schippen 7")
    if random_karte == 8 and random_farbe == "Schippe":
        print("Schippen 8")
    if random_karte == 9 and random_farbe == "Schippe":
        print("Schippen 9")
    if random_karte == 1 and random_farbe == "Schippe":
        print("Schippen Ass")
    if random_karte == 1 and random_farbe == "Schippe":
        print("Schippen Ass")
    if random_karte == 1 and random_farbe == "Schippe":
        print("Schippen Ass")
    if random_karte == 1 and random_farbe == "Schippe":
        print("Schippen Ass")





























