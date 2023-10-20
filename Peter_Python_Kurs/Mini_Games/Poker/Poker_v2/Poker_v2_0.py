import time
from fnc_worthing_new import *
money = 10000
# Loop beginn


def statistics():
    print(
        f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Poker: Texas hold'em |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  # nopep8
    print(f"\t\t\t\t\t\t\t|--- Round: ----------------------------- {runde}")
    print(f"\t\t\t\t\t\t\t|--- Your Money: ------------------------ {money:,} €")
    print(f"\t\t\t\t\t\t\t|--- Your Cards: ------------------------ {player_own}")
    print(
        f"\t\t\t\t\t\t\t|-------------------------------------------------------------------------------------------")  # nopep8
    print(f"\t\t\t\t\t\t\t|--- In the Pot: ------------------------ {pot_money:,} €")
    print(f"\t\t\t\t\t\t\t|--- Opponets money in the Pot:---------- {opponet_pot_money} €")
    print(f"\t\t\t\t\t\t\t|--- Your money in the Pot: ------------- {own_pot_money:,} €")
    print(
        f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Poker: Texas hold'em |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  # nopep8
    print("\n")


def user_raise_input():
    global own_pot_money
    global pool_raise
    global blind
    global money
    global opponet_pot_money
    if own_pot_money == opponet_pot_money:
        print("Everyone has the same money in the pot right now!")
    pool_raise = int(input(f"How much money do you want to lay in the pool:\t"))
    if own_pot_money != opponet_pot_money:  # pot_money_list[0] ist das höchste im pot
        while pool_raise < blind or pool_raise > money:
            pool_raise = int(input(f"How much money do you want to lay in the pool:\t"))
    elif pool_raise == 0:
        return True
    documetary_own_money(pool_raise)


def opponent_raise():
    global pot_money_list
    global pot_money
    global opponet_pot_money
    opponet_raise = random.choices(opponets_raise_chances, weights=[5, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    for char in opponet_raise:
        opponet_raise = int(char)
    print(f'''_______________________________________________________
                Your opponent raised the pot with {opponet_raise} $\n''')
    pot_money += opponet_raise
    opponet_pot_money += opponet_raise
    pot_money_list.append(opponet_raise)
    pot_money_list.sort(reverse=True)


def opponent_goes_with_u():
    global pot_money
    global opponet_pot_money
    print("You now are higher than your opponent!")
    time.sleep(1)
    print("Your opponet goes with you!")
    opponet_pot_money = own_pot_money
    pot_money = opponet_pot_money + own_pot_money
    time.sleep(2)


def give_cards(count=2):
    global card_list
    hand = []
    while len(hand) != count:
        card = random.choices(card_list, k=1)
        for current_card_in_def_give_cards in card:
            card_list.remove(current_card_in_def_give_cards)
        hand.extend(card)
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
runde = 0
blind = 10
opponets_raise_chances = [blind*0, blind*0, blind*0, blind*0, blind*0, blind*0, blind*2, blind*3, blind*4, blind*5]  # nopep8
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
        pool_raise = 0
        opponet_pot_money = pot_money - own_pot_money
        if own_pot_money > opponet_pot_money:  # wenn du mehr als dein gegner im pot hast
            opponent_goes_with_u()

        else:
            opponent_raise()
        statistics()

        user_raise_input()

        if pool_raise == 0:
            break

        documetary_own_money(pool_raise)
        statistics()

    print("The next Round beginns!")
    print("Open Cards:\t\t", end="")
    print(f"{table_cards[0:runde + 2]}\n")

    time.sleep(2)
    pot_money_list.sort(reverse=True)

# Berechnungen...
print("Berechnung")

print(f"\n\nTable Cards:\t\t{sorted(table_cards, key=custom_sort, reverse=True)}")
print(f"Own Cards:\t\t\t{sorted(player_own, key=custom_sort, reverse=True)}")
print(f"Opponent Cards:\t\t{sorted(player_1, key=custom_sort, reverse=True)}")
