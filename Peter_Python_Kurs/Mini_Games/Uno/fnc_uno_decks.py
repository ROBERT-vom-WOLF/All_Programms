import random
import time


def print_hand():
    global oberste_karte
    global kartenstapel
    global player_1
    global player_2
    global current_player
    oberste_karte = kartenstapel[-1]
    nummer = 0
    if current_player % 2 == 0:
        print("Die aktionen deines Gegners:", end="\t\t")
        for char1 in player_1_log:
            print(char1, end=", ")
        print(f"\nDein gegner hat noch {len(player_2)} Karten!")
        if len(player_2) == 1:
            print("UNO")
        print("\nSpieler 1:\n")
        for char1 in player_1:
            nummer += 1
            char1 = str(char1)
            print(f"{nummer}.\t{char1}")
    else:
        print("Die aktionen deines Gegners:", end="\t\t")
        for char1 in player_1_log:
            print(char1, end=", ")
        print(f"\nDein gegner hat noch {len(player_1)} Karten!")
        if len(player_2) == 1:
            print("UNO")
        print("\nSpieler 2:\n")
        for char1 in player_2:
            nummer += 1
            print(f"{nummer}.\t{char1}")
    print(f"\nOberste Karte:\t{oberste_karte}")


def give_card(count=1):
    global kartenstapel
    card_deck = []
    vzhsud = 0
    while vzhsud != count:
        card = random.choices(kartenstapel, k=1)
        for char2 in card:
            kartenstapel.remove(char2)
        card_deck.extend(card)
        vzhsud += 1
    return card_deck


def move(spielerhand):
    global kartenstapel
    global player_1
    global player_2
    global current_player
    global oberste_karte
    oberste_karte = kartenstapel[-1]
    possible_moves = 0
    for char3 in spielerhand:
        char3 = str(char3)
        if char3[8:9] in oberste_karte[8:9]:
            possible_moves += 1
        elif char3[0:1] in oberste_karte[0:1]:
            possible_moves += 1
    if possible_moves == 0:
        print("Du hast keine Karte, die du legen darfst!")
        print('Nutze den befehl: "pull" um eine neue Karte zu ziehen!')

    while True:
        answer = input("Dein Karte:\t\t")
        if answer.lower() == "pull" and possible_moves == 0:
            print("Du ziehst eine Karte!")
            if current_player % 2 == 0:
                player_1.extend(give_card())
                nummer = 0
                for char3 in player_1:
                    nummer += 1
                    char3 = str(char3)
                    print(f"{nummer}.\t{char3}")
                return answer
            else:
                player_2.extend(give_card())
                nummer = 0
                for char3 in player_2:
                    nummer += 1
                    char3 = str(char3)
                    print(f"{nummer}.\t{char3}")
                return answer
        else:
            answer = int(answer)
            karte1 = str(spielerhand[answer - 1])
            if karte1[0:1] in oberste_karte[0:1]:
                print(f"Du hast gelegt:\t{karte1}")
                kartenstapel.append(karte1)
                return karte1
            elif karte1[8:9] in oberste_karte[8:9]:
                print(f"Du hast gelegt:\t{karte1}")
                kartenstapel.append(karte1)
                return karte1
            else:
                print(f'"Error bei Eingabe: {karte1}!\nNicht möglicher Spielzug!')


def wechsel(counter=True):
    global current_player
    for char4 in range(0, 1):
        print("\n")
    print("Wechsel nun den Platz mit deinem Gegenspieler!")
    time.sleep(3)
    if counter:
        for char4 in range(0, 1000000):
            print("\n")
        aafjndjhzsdhan = 10
        for char4 in range(0, 10):
            print(f"Wechsel in:   {aafjndjhzsdhan} Sekunden!")
            time.sleep(1)
            aafjndjhzsdhan -= 1
        for char4 in range(0, 1000000):
            print("\n")
    for char4 in range(0, 1):
        print("\n")


def rules():
    global kartenstapel
    global player_1
    global player_2
    global oberste_karte
    global current_player
    oberste_karte = kartenstapel[len(kartenstapel) - 1]
    if len(player_1) == 0 or len(player_2) == 0:
        print("Uno Uno!")
        exit()
    if oberste_karte[8:9] != "S" and oberste_karte[8:9] != "R" or "pull" in oberste_karte:
        current_player += 1
        if current_player % 2 == 0:
            if "+2" in oberste_karte and "+" not in player_1:
                for _ in range(0, 2):
                    player_1.extend(give_card())
            if "+4" in oberste_karte and "+" not in player_1:
                for _ in range(0, 4):
                    player_1.extend(give_card())
        if current_player % 2 == 1:
            if "+2" in oberste_karte and "+" not in player_2:
                for _ in range(0, 2):
                    player_2.extend(give_card())
            if "+4" in oberste_karte and "+" not in player_2:
                for _ in range(0, 4):
                    player_2.extend(give_card())

        if "+4" in oberste_karte:
            answer = 0
            while answer > 4 or answer < 1:
                print("Welche Farbe wünschts du dir?")
                answer = int(input("[1]Blue, [2]Red, [3]Green oder [4]Yellow?\t"))
            if answer == "1":
                kartenstapel.append("Blue    ?")
            if answer == "2":
                kartenstapel.append("Red     ?")
            if answer == "3":
                kartenstapel.append("Green   ?")
            if answer == "4":
                kartenstapel.append("Yellow  ?")
        wechsel()
    else:
        print("Du darfst nochmal!")


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
    "Yellow  +2",
    "Yellow  +4",
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
# decks = int(input("Wie viele Decks willst du verwenden?\t\t"))
# cards_count = int(input("Wie viele Karten soll jeder haben?\t\t\t"))
decks = 1
cards_count = 5
kartenstapel = []
durchgang = 0
current_player = 0
while True:
    durchgang += 1
    kartenstapel.extend(cards_liste)
    if durchgang == decks:
        break
player_1 = give_card(cards_count)
player_2 = give_card(cards_count)
player_1 = sorted(player_1)
player_2 = sorted(player_2)
player_1_log = []
player_2_log = []
random.shuffle(kartenstapel)

while True:
    for char in range(0, 10):
        print("\n")
    oberste_karte = kartenstapel[-1]
    if current_player % 2 == 0:
        print_hand()
        karte = move(player_1)
        player_1_log.append(karte)
        if karte == "pull":
            karte = move(player_1)
        if karte != "pull":
            player_1.remove(karte)
        time.sleep(3)
        rules()

    else:
        print_hand()
        karte = move(player_2)
        player_2_log.append(karte)
        if karte == "pull":
            karte = move(player_2)
        if karte != "pull":
            player_2.remove(karte)
        time.sleep(3)
        rules()
