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
values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


def give_cards(count=2):
    global card_list
    hand = []
    while len(hand) != count:
        card = random.choices(card_list, k=1)
        for char in card:
            card_list.remove(char)
        hand.extend(card)
    return hand


def return_number(string):
    if string[9:10] == "A":
        return "14"

    elif string[9:10] == "K":
        return "13"

    elif string[9:10] == "Q":
        return "12"

    elif string[9:10] == "J":
        return "11"

    elif string[9:10] == "T":
        return "10"

    elif string[9:10] == "9":
        return "9"

    elif string[9:10] == "8":
        return "8"

    elif string[9:10] == "7":
        return "7"

    elif string[9:10] == "6":
        return "6"

    elif string[9:10] == "5":
        return "5"

    elif string[9:10] == "4":
        return "4"

    elif string[9:10] == "3":
        return "3"

    elif string[9:10] == "2":
        return "2"


def find_duplicates(list):
    duplicates = []
    already_documented = []
    for char in list:
        count = list.count(char)
        if count > 1:
            if char not in already_documented:
                duplicates.append(count)
                already_documented.append(char)
    return duplicates


def custom_sort(card):
    return values[card[9:10]]


def create_number_list(liste):
    number_list = []
    for char in liste:
        char = return_number(char)
        number_list.append(char)
    return number_list


table_cards = give_cards(5)
player_own = give_cards()
player_1 = give_cards()
print(f"\n\nTable Cards:\t\t{sorted(table_cards, key=custom_sort, reverse=True)}")
print(f"Own Cards:\t\t\t{sorted(player_own, key=custom_sort, reverse=True)}")
print(f"Opponent Cards:\t\t{sorted(player_1, key=custom_sort, reverse=True)}")


def return_duplicates(list):
    duplicates = ""
    pairs = 0
    threes = 0
    for char in list:
        if list.count(char) == 3:
            duplicates = "three of a kind"
        elif list.count(char) == 2 and threes == 0:
            duplicates = "pair"
            pairs += 1

    if pairs == 4 and threes == 3:
        duplicates = "Full House"
    if pairs == 4 and threes == 0:
        duplicates = "two pair"

    return duplicates


def worthing_best_five(open, own, opponent):
    cards_7_own = open + own
    cards_7_opponent = open + opponent
    cards_7_all = open + own + opponent
    cards_7_own = sorted(cards_7_own, key=custom_sort, reverse=True)
    cards_7_opponent = sorted(cards_7_opponent, key=custom_sort, reverse=True)
    cards_7_all = sorted(cards_7_all, key=custom_sort, reverse=True)
    cards_7_own_num = create_number_list(cards_7_own)
    cards_7_opponent_num = create_number_list(cards_7_opponent)
    cards_7_all_num = create_number_list(cards_7_all)

    if cards_7_all[0] in own:
        print("Du hast high card!")

    elif cards_7_all[0] in opponent:
        print("Dein gegner hat High Card!")

    else:
        print("Die high card liegt offen!")

    print(cards_7_own_num)
    print(cards_7_opponent_num)

    print(f"You : {return_duplicates(cards_7_own_num)}")
    print(f"Bro : {return_duplicates(cards_7_opponent_num)}")


worthing_best_five(table_cards, player_own, player_1)
