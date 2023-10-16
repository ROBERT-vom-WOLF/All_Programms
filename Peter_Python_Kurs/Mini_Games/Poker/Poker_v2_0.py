import random
import time
money = 10000
# Loop beginn
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


def documetary_own_money(document):
    global pot_money_list
    global pot_money
    global own_pot_money
    global money
    pot_money_list.append(document)
    money -= document
    own_pot_money += document
    pot_money += document
    pot_money_list.sort(reverse=True)

pot_money_list = []
pot_money = 0
own_pot_money = 0
table_cards = give_cards(5)
player_own = give_cards(2)
player_1 = give_cards(2)
player_2 = give_cards(2)
runde = 0
blind = 10
yes_or_no = [1, 0]
opponets_raise_chances = [blind*0, blind*2, blind*3, blind*4, blind*5, blind*6, blind*7, blind*8, blind*9, blind*10]
print(f"You currently have {money:,} $ in your Account!\n")
print(f"The Blind is currently: {blind:,} $\n")
print("Do you want to play this round?")
play_request = input("[Y]es or [N]o \t")
if play_request.lower() == "n":
    print("You paused for a round!")
    exit()  # später wird aus dem exit ein break gemacht, wenn alles in einer loop ist
documetary_own_money(blind)
time.sleep(0.5)
print("Your opponent goes with you and lies 10 $ in!\n")
pot_money += 10
pot_money_list.append(10)
pot_money_list.sort(reverse=True)
time.sleep(0.8)
while True:
    runde += 1
    if runde >= 4:
        break
    while True:
        if own_pot_money > pot_money - own_pot_money:  # wenn du mehr als dein gegner im pot hast
            print("you now overbit your opponent!")
            time.sleep(1)
            if random.choices(yes_or_no, weights=[3, 1]) == 1:
                print("Your opponet goes with you!")
                pot_money = own_pot_money
            else:
                print("He throws!")
                exit()  # später wird aus dem exit ein break gemacht, wenn alles in einer loop ist

        print("Its your opponets turn!")
        time.sleep(2)
        opponet_raise = random.choices(opponets_raise_chances, weights=[5, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        for char in opponet_raise:
            opponet_raise = int(char)
        print(f"Your opponent raised the pot with {opponet_raise} $")
        pot_money += opponet_raise
        pot_money_list.append(opponet_raise)
        pot_money_list.sort(reverse=True)
        print(f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Poker: Texas hold'em |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   # nopep8
        print(f"\t\t\t\t\t\t\t|--- Round: ----------------------------- {runde}")
        print(f"\t\t\t\t\t\t\t|--- Your Money: ------------------------ {money:,} €")
        print(f"\t\t\t\t\t\t\t|--- Your Cards: ------------------------ {player_own}")
        print(f"\t\t\t\t\t\t\t|-------------------------------------------------------------------------------------------")   # nopep8
        print(f"\t\t\t\t\t\t\t|--- In the Pot: ------------------------ {pot_money:,} €")
        print(f"\t\t\t\t\t\t\t|--- Opponets money in the Pot:---------- {pot_money - own_pot_money} €")
        print(f"\t\t\t\t\t\t\t|--- Your money in the Pot: ------------- {own_pot_money:,} €")
        print(f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Poker: Texas hold'em |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   # nopep8
        print("\n")
        if own_pot_money == pot_money_list[0]:
            print("Everyone has the same money in the pot right now!")
        pool_raise = int(input(f"How much money do you want to lay in the pool:\t"))
        while own_pot_money + pool_raise < pot_money_list[0]:  # pot_money_list[0] ist das höchste im pot
            while pool_raise < blind or pool_raise > money:
                pool_raise = int(input(f"How much money do you want to lay in the pool:\t"))
        documetary_own_money(pool_raise)
        if own_pot_money == pot_money_list[0]:
            break
        print(f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Poker: Texas hold'em |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   # nopep8
        print(f"\t\t\t\t\t\t\t|--- Round: ----------------------------- {runde}")
        print(f"\t\t\t\t\t\t\t|--- Your Money: ------------------------ {money:,} €")
        print(f"\t\t\t\t\t\t\t|-------------------------------------------------------------------------------------------")   # nopep8
        print(f"\t\t\t\t\t\t\t|--- In the Pot: ------------------------ {pot_money:,} €")
        print(f"\t\t\t\t\t\t\t|--- Opponets money in the Pot:---------- {pot_money - own_pot_money} €")
        print(f"\t\t\t\t\t\t\t|--- Your money in the Pot: ------------- {own_pot_money:,} €")
        print(f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Poker: Texas hold'em |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   # nopep8
        print("\n")

    print("The next Round beginns!")
    print("Open Cards:\t\t", end="")
    print(f"{table_cards[0:runde + 2]}\n")

    time.sleep(2)
    pot_money_list.sort(reverse=True)
# Berechnungen...
print("Berechnung")
