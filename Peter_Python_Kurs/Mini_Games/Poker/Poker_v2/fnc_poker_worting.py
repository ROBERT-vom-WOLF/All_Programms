import random

card_list = [
    "Herz     A",
    "Herz     K",
    "Herz     Q",
    "Herz     J",
    "Herz     T",
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
    "Schippe  T",
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
    "Blatt    T",
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
    "Raute    T",
    "Raute    9",
    "Raute    8",
    "Raute    7",
    "Raute    6",
    "Raute    5",
    "Raute    4",
    "Raute    3",
    "Raute    2"
]


def give_cards(count=2):
    global card_list
    hand = []
    while True:
        card = random.choices(card_list, k=1)
        for char in card:
            card_list.remove(char)
        if len(hand) != count:
            hand.extend(card)
        else:
            return hand


table_cards = give_cards(5)
player_own = give_cards(2)
player_1 = give_cards(2)
print(player_own)
print(player_1)
print(table_cards)


def sort_bild(string):
    if "A" in string:
        return 1
    else:
        return -1


def singe_worthing(string):
    if string[9:10] == "A":
        return 11

    elif string[9:10] == "K":
        return 10

    elif string[9:10] == "Q":
        return 10

    elif string[9:10] == "J":
        return 10

    elif string[9:10] == "T":
        return 10

    elif string[9:10] == "9":
        return 9

    elif string[9:10] == "8":
        return 8

    elif string[9:10] == "7":
        return 7

    elif string[9:10] == "6":
        return 6

    elif string[9:10] == "5":
        return 5

    elif string[9:10] == "4":
        return 4

    elif string[9:10] == "3":
        return 3

    elif string[9:10] == "2":
        return 2


def worthing():
    global table_cards
    global player_own
    global player_1
    print("Proccesing...")
    table_cards.sort(key= lambda k: k, reverse=True)
    player_own.sort(key=lambda k: k[9:10], reverse=True)
    player_1.sort(key=lambda k: k[9:10], reverse=True)
    print(f"Table:\t\t\t{table_cards}")
    print(f"Own:\t\t\t{player_own}")
    print(f"Player:\t\t\t{player_1}")


worthing()

