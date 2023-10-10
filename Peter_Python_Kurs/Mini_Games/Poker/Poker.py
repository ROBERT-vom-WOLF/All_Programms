import random
import time
card_list = [
    "Herz     A",
    "Herz     K",
    "Herz     Q",
    "Herz     J",
    "Herz     10",
    "Herz     9",
    "Herz     8",
    "Herz     7",
    "Herz     6",
    "Herz     5",
    "Herz     4",
    "Herz     3",
    "Herz     2",
    "Schippe  A",
    "Schippe  K",
    "Schippe  Q",
    "Schippe  J",
    "Schippe  10",
    "Schippe  9",
    "Schippe  8",
    "Schippe  7",
    "Schippe  6",
    "Schippe  5",
    "Schippe  4",
    "Schippe  3",
    "Schippe  2",
    "Blatt    A",
    "Blatt    K",
    "Blatt    Q",
    "Blatt    J",
    "Blatt    10",
    "Blatt    9",
    "Blatt    8",
    "Blatt    7",
    "Blatt    6",
    "Blatt    5",
    "Blatt    4",
    "Blatt    3",
    "Blatt    2",
    "Raute    A",
    "Raute    K",
    "Raute    Q",
    "Raute    J",
    "Raute    10",
    "Raute    9",
    "Raute    8",
    "Raute    7",
    "Raute    6",
    "Raute    5",
    "Raute    4",
    "Raute    3",
    "Raute    2"
]

dealed_card = 0
cards = []
print("Eigene Hand:", end="\t\t")
player_own = random.choices(card_list, k=2)

for char in player_own:
    print(char, end="\n\t\t\t\t\t")
    card_list.remove(char)
print("\n")

time.sleep(2)
cards += random.choices(card_list, k=3)
print("Ausgelegt:", end="\t\t\t")
for char_0 in cards:
    print(char_0, end="\n\t\t\t\t\t")
    card_list.remove(char_0)
dealed_card += 3


while True:
    dealed_card += 1
    if dealed_card == 6:
        break
    input("\nNächste Runde\n")

    cards += random.choices(card_list, k=1)
    print("Ausgelegt:", end="\t\t\t")
    char_0 = ""
    for char_0 in cards:
        print(char_0, end="\n\t\t\t\t\t")
    card_list.remove(char_0)
    time.sleep(2)

input("\nLetzte Runde\n")
print("Ausgelegt:", end="\t\t\t")
for char_last_round in cards:
    print(char_last_round, end="\n\t\t\t\t\t")

input("\n\nAufdecken!\n")
time.sleep(2)

player_1 = random.choices(card_list, k=2)
print("\nSpieler 1:\t", end="")
for char_1 in player_1:
    print(char_1, end="; ")
    card_list.remove(char_1)
time.sleep(2)


player_2 = random.choices(card_list, k=2)
print("\nSpieler 2:\t", end="")
for char_2 in player_2:
    print(char_2, end="; ")
    card_list.remove(char_2)
time.sleep(2)


player_3 = random.choices(card_list, k=2)
print("\nSpieler 3:\t", end="")
for char_3 in player_3:
    print(char_3, end="; ")
    card_list.remove(char_3)
time.sleep(2)


player_4 = random.choices(card_list, k=2)
print("\nSpieler 4:\t", end="")
for char_4 in player_4:
    print(char_4, end="; ")
    card_list.remove(char_4)
time.sleep(2)
