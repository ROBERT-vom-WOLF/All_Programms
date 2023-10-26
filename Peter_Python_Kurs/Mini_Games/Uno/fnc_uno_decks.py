import random

cards_liste = [
    "G  0",
    "G  1",
    "G  2",
    "G  3",
    "G  4",
    "G  5",
    "G  6",
    "G  7",
    "G  8",
    "G  9",
    "G -Skip",
    "G -Reverse",
    "G +2",
    "G +4",
    "Y  0",
    "Y  1",
    "Y  2",
    "Y  3",
    "Y  4",
    "Y  5",
    "Y  6",
    "Y  7",
    "Y  8",
    "Y  9",
    "Y -Skip",
    "Y -Reverse",
    "Y +2",
    "Y +4",
    "R  0",
    "R  1",
    "R  2",
    "R  3",
    "R  4",
    "R  5",
    "R  6",
    "R  7",
    "R  8",
    "R  9",
    "R -Skip",
    "R -Reverse",
    "R +2",
    "R +4",
    "B  0",
    "B  1",
    "B  2",
    "B  3",
    "B  4",
    "B  5",
    "B  6",
    "B  7",
    "B  8",
    "B  9",
    "B -Skip",
    "B -Reverse",
    "B +2",
    "B +4"]

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
        for char_zgahsbhbhb in card:
            all_decks.remove(char_zgahsbhbhb)
        count -= 1
    return card_deck


player_1 = give_card(cards_count)
player_2 = give_card(cards_count)
random.shuffle(all_decks)
oberste_karte = all_decks[0]
while True:
    if current_player_1:
        print("Spieler 1 ist am Zug!\n")
        for char in player_1:
            print(char)

    elif not current_player_1:
        print("Spieler 2 ist am Zug!\n")
        for char in player_2:
            print(char)

    else:
        print("Error kein Boolean type")
        exit()

    print(f"Oberste Karte:\t{oberste_karte}")
    user_input = "System, user_input char naming syntax type string"
    while user_input[3:4] != oberste_karte[3:4] or user_input[0:1] != oberste_karte[3:4]:
        user_input = input("Du legst ab:\t\t")
