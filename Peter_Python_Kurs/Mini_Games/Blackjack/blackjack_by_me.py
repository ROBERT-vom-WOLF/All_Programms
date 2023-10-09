import random
import time
from blackjack_card_system import *
from fnc_ask_again import *
while True:
    cards = random.choices(cards_list, k=2)
    kartenwert = 0
    dealer_worth = 0
    dealer_hand = []
    user = ""
    while True:
        while kartenwert < 100:
            kartenwert = 0
            print(f"Deine Karten:", end="\t\t\t")
            for char in cards:
                print(char, end=" ")
                kartenwert += worth(char)
            print(f"\nKartenwert:\t\t\t\t{kartenwert}")
            if kartenwert == 21:
                print("Du hast ein Blackjack!")
                print("Gewonnen!")
                break
            if kartenwert > 21:
                print("Du hast verloren!")
                kartenwert = 100
                break
            user = input("\n\nMoechtest du [Z]iehen, [K]lopfen oder [W]erfen?\t").lower()
            if user.lower() == "z":
                cards.extend(random.choices(cards_list, k=1))
            elif user.lower() == "k":
                while dealer_worth < 21:
                    dealer_card = random.choices(cards_list, k=1)
                    dealer_hand += dealer_card
                    dealer_worth += worth(dealer_card)
                    print(f"Der Dealer zeiht eine Karte!")
                    time.sleep(1.2)
                    print(f"Es ist:                        {dealer_card}")
                    print(f"Zusammen ergeben seine Karten: {dealer_worth}\n")
                    time.sleep(2)
                if dealer_worth == 21:
                    print("Der dealer hat gewonnen")
                    print("Du hast gewonnen!")
                    break
                if dealer_worth > 21:
                    print("Der dealer hat verloren")
                    print("Du hast gewonnen!")
                    break
            elif user.lower() == "w":
                print("Du hast geworfen!")
                print("Viel Glück bei der nächsten Runde!")
        break
    ask("spielen", "DE")
