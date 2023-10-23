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


# table_cards = give_cards(5)
# player_own = give_cards()
# player_1 = give_cards()
# print(f"\n\nTable Cards:\t\t{sorted(table_cards, key=custom_sort, reverse=True)}")
# print(f"Own Cards:\t\t\t{sorted(player_own, key=custom_sort, reverse=True)}")
# print(f"Opponent Cards:\t\t{sorted(player_1, key=custom_sort, reverse=True)}")


def return_duplicates(list):
    duplicates = ""
    pairs = 0
    threes = 0
    fours = 0
    for char in list:
        if list.count(char) == 4:
            duplicates = "8: four of a kind"
            fours += 1
        if list.count(char) == 3:
            duplicates = "4: three of a kind"
            threes += 1
        if list.count(char) == 2:
            duplicates = "2: pair"
            pairs += 1
    if fours == 4:
        duplicates = "8: four of a kind"
    elif pairs == 2 and threes == 3:
        duplicates = "7: Full House"
    elif pairs == 4:
        duplicates = "3: two pair"
    print(f"Pairs: {pairs}", end="\t")
    print(f"Threes: {threes}", end="\t")
    print(f"Fours: {fours}")
    return duplicates


def compinations(list, number_list, all_number_list):
    herzen = 0
    blatt = 0
    schippe = 0
    raute = 0
    pairs = 0
    threes = 0
    fours = 0
    straight_list = []
    durchlauf = 0
    for straight_char in number_list:
        straight_char = int(straight_char)
        straight_char += durchlauf
        straight_list.append(straight_char)
        durchlauf += 1
    # print(straight_list)
    for char in list:
        if char[0:1] == "H":
            herzen += 1
        if char[0:1] == "R":
            raute += 1
        if char[0:1] == "B":
            blatt += 1
        if char[0:1] == "S":
            schippe += 1
    for char_2 in number_list:
        ammount = number_list.count(char_2)
        if ammount >= 4:
            fours += 1
        if ammount >= 3:
            threes += 1
        if ammount >= 2:
            pairs += 1
    all_value = 0
    for char in number_list:
        char = int(char)
        all_value += char
    if (herzen >= 5 or schippe >= 5 or blatt >= 5 or raute >= 5) and number_list == {14, 13, 12, 11, 10}:
        return f"10: Royal Flush {all_value}"
    elif (straight_list.count(straight_list[0]) == 5 or straight_list.count(straight_list[1]) == 5 or straight_list.count(straight_list[2]) == 5) and (herzen == 5 or schippe == 5 or blatt == 5 or raute == 5):  # nopep8
        return f"9: straight flush {all_value}"
    elif fours >= 4:
        return f"8: four of a kind {all_value}"
    elif pairs >= 2 and threes >= 3:
        return f"7: Full House {all_value}"
    elif herzen >= 5 or schippe >= 5 or blatt >= 5 or raute >= 5:
        return f"6: Flush {all_value}"
    elif straight_list.count(straight_list[0]) == 5 or straight_list.count(straight_list[1]) == 5 or straight_list.count(straight_list[2]) == 5:  # nopep8
        return f"5: straight {all_value}"
    elif threes >= 3:
        return f"4: three of a kind {all_value}"
    elif pairs >= 4:
        return f"3: two pair {all_value}"
    elif pairs >= 2:
        return f"2: pair {all_value}"
    elif all_number_list[0] == number_list[0]:
        return f"1: High Card {all_value}"
    else:
        return "0"


def worthing_best_five(open, own, opponent):
    cards_7_own = open + own
    cards_7_opponent = open + opponent
    cards_7_all = open + own + opponent
    cards_7_own = sorted(cards_7_own, key=custom_sort, reverse=True)
    cards_7_opponent = sorted(cards_7_opponent, key=custom_sort, reverse=True)
    cards_7_all = sorted(cards_7_all, key=custom_sort, reverse=True)
    cards_7_all_num = create_number_list(cards_7_all)
    cards_7_own_num = create_number_list(cards_7_own)
    cards_7_opponent_num = create_number_list(cards_7_opponent)
    # cards_7_own_num = ['14', '13', '12', '11', '10', '9', '8']
    # cards_7_opponent_num = ['12', '11', '10', '8', '7', '6', '4']

    # print(cards_7_own_num)
    # print(cards_7_opponent_num)
    own_worthing = compinations(cards_7_own, cards_7_own_num, cards_7_all_num)
    opponents_worthing = compinations(cards_7_opponent, cards_7_opponent_num, cards_7_all_num)
    print(f"You:    {own_worthing}")
    print(f"Bro:    {opponents_worthing}")
    if opponents_worthing[0] == own_worthing[0]:
        if int(opponents_worthing[13:]) < int(opponents_worthing[13:]):
            print("Du hast gewonnen!")
        elif int(opponents_worthing[13:]) > int(opponents_worthing[13:]):
            print("Dein gegner hat gewonnen!")
        else:
            print("Draw!")
    elif int(opponents_worthing[0]) > int(own_worthing[0]):
        print("Dein gegner hat gewonnen!")
    elif int(opponents_worthing[0]) < int(own_worthing[0]):
        print("Du hast gewonnen!")


# worthing_best_five(table_cards, player_own, player_1)


