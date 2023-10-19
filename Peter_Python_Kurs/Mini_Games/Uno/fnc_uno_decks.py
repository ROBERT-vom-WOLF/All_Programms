import random

cards_liste = [
    "Green   0",
    "Green   1",
    "Green   2",
    "Green   3",
    "Green   4",
    "Green   5",
    "Green   6",
    "Green   7",
    "Green   8",
    "Green   9",
    "Green   Skip",
    "Green   Reverse",
    "Green   +2",
    "Green   +4",
    "Yellow  0",
    "Yellow  1",
    "Yellow  2",
    "Yellow  3",
    "Yellow  4",
    "Yellow  5",
    "Yellow  6",
    "Yellow  7",
    "Yellow  8",
    "Yellow  9",
    "Yellow  Skip",
    "Yellow  Reverse",
    "Yellow +2",
    "Yellow +4",
    "Red     0",
    "Red     1",
    "Red     2",
    "Red     3",
    "Red     4",
    "Red     5",
    "Red     6",
    "Red     7",
    "Red     8",
    "Red     9",
    "Red     Skip",
    "Red     Reverse",
    "Red     +2",
    "Red     +4",
    "Blue    0",
    "Blue    1",
    "Blue    2",
    "Blue    3",
    "Blue    4",
    "Blue    5",
    "Blue    6",
    "Blue    7",
    "Blue    8",
    "Blue    9",
    "Blue    Skip",
    "Blue    Reverse",
    "Blue    +2",
    "Blue    +4",
               ]
decks = int(input("Wie viele Decks willst du verwenden?\t\t"))
cards_count = int(input("Wie viele Karten willst du verwenden?\t\t"))
all_decks = []
durchgang = 0
current_player_1 = True
while True:
    durchgang += 1
    all_decks.extend(cards_liste)
    if durchgang == decks:
        break


def give_card(count=1):
    global all_decks
    card_deck = []
    while count > 0:
        card = random.choices(all_decks, k=1)
        card_deck += card
        for char in card:
            all_decks.remove(char)
        count -= 1
    return card_deck


player_1 = give_card(cards_count)
player_2 = give_card(cards_count)
player_1 = sorted(player_1)
player_2 = sorted(player_2)
random.shuffle(all_decks)

if current_player_1:
    print("Spieler 1 ist am Zug!\n")
    for char in player_1:
        print(char)
    print(f"\nOberste Karte:\t{all_decks[0]}")
elif not current_player_1:
    print("Spieler 2 ist am Zug!\n")
    for char in player_2:
        print(char)
    print(f"\nOberste Karte:\t{all_decks[0]}")

else:
    print("Error kein Boolean type")
    exit()
