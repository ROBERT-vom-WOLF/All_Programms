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


own_cards = ["Herz     A", "Herz     B"]
open_cards = ["Herz     A", "Herz     B", "", "", ""]
doubles = 0
tripples = 0
for char_1 in open_cards:
    for char_2 in own_cards:
        if char_1[9:10] == char_2[9:10]:
            doubles += 1
            print("Double")
card_1_own = own_cards[0]
card_2_own = own_cards[1]
card_1_open = open_cards[0]
card_2_open = open_cards[1]
card_3_open = open_cards[2]
card_4_open = open_cards[3]
card_5_open = open_cards[4]
if doubles > 1:
    if card_1_own[9:10] == card_2_own[9:10]:
        print("Tripple")
        doubles /= 2
        doubles -= 1
        tripples += 1
    elif card_1_own[9:10] == card_1_open and card_2_own == card_2_open:
        print("Two Pairs")
if doubles > 1:
    if card_1_open[9:10] == card_2_open[9:10]:
        print("Tripple")
        doubles /= 2
        doubles -= 1
        tripples += 1
    else:
        print("Two Pairs")
