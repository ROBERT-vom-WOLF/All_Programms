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

    else:
        print("SYSTEM ERROR: TYPER ERROR IN FNC: RETURN NUMBER")
        print("SYSTEM ERROR: SHUTDOWN!")
        exit()


def custom_sort(card):
    return values[card[9:10]]


def create_number_list(liste):
    number_list = []
    for char in liste:
        char = return_number(char)
        number_list.append(char)
    return number_list


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
    same_color = False
    straight = False
    if herzen >= 5 or schippe >= 5 or blatt >= 5 or raute >= 5:
        same_color = True
    if straight_list.count(straight_list[0]) == 5 or straight_list.count(straight_list[1]) == 5 or straight_list.count(straight_list[2]) == 5:   # nopep8
        straight = True

    if same_color and number_list == {14, 13, 12, 11, 10}:
        return "10: Royal Flush"
    elif same_color and straight:
        return "9: straight flush"
    elif fours >= 4:
        return "8: four of a kind"
    elif pairs >= 2 and threes >= 3:
        return "7: Full House"
    elif herzen >= 5 or schippe >= 5 or blatt >= 5 or raute >= 5:
        return "6: Flush"
    elif straight:
        return "5: straight"
    elif threes >= 3:
        return "4: three of a kind"
    elif pairs >= 4:
        return "3: two pair"
    elif pairs >= 2:
        return "2: pair"
    elif all_number_list[0] == number_list[0]:
        return "1: High Card"
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
    own_worthing = compinations(cards_7_own, cards_7_own_num, cards_7_all_num)
    opponents_worthing = compinations(cards_7_opponent, cards_7_opponent_num, cards_7_all_num)
    print(f"You:    {own_worthing[3:12]}")
    print(f"Bro:    {opponents_worthing[3:12]}")
    if opponents_worthing[0] == own_worthing[0]:
        print("Draw")
        return 0
    elif int(opponents_worthing[0]) > int(own_worthing[0]):
        print("Dein gegner hat gewonnen!")
        return -1
    elif int(opponents_worthing[0]) < int(own_worthing[0]):
        print("Du hast gewonnen!")
        return 1
