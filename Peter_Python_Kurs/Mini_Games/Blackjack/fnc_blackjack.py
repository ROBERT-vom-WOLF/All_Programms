def blackjack(graphics_on_off=""):
    import random
    import time
    import fnc_blackjack_werte
    blackjack_greeting = ""

    if graphics_on_off != "on":
        blackjack_greeting = "Black Jack"

    print("\t\t\t\t\tHerzlich Willkommen im Kasino!")
    print(f"\t\t\t\t\tHeute spielen wir: {blackjack_greeting}")
    time.sleep(1.5)

    if graphics_on_off == "on":
        print('''
        ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗   ░░░░░██╗░█████╗░░█████╗░██╗░░██╗
        ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝   ░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
        ██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░   ░░░░░██║███████║██║░░╚═╝█████═╝░
        ██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░   ██╗░░██║██╔══██║██║░░██╗██╔═██╗░
        ██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗   ╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
        ╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝   ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
        ''')
    time.sleep(1.5)
    wins = 0
    losses = 0
    black_jacks = 0
    money = 2000
    blind = 100
    runde = 0
    ueberboten = False

    while True:
        runde += 1
        # cards = random.choices(cards_list, weights=[10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k=1)
        # cards += random.choices(cards_list, weights=[0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k=1)
        cards = random.choices(fnc_blackjack_werte.cards_list, k=2)
        dealer_worth = 0
        dealer_hand = []
        user = ""
        if money <= 0:
            print("Sie haben kein geld mehr!")
            exit()

        if runde % 5 == 0:
            blind += 10
            print(f"\nEs ist Runde: {runde}")
            print(f"Der Blind wurde erhöt\n")

        while True:
            kartenwert = 0
            blind_throw = 0
            print(f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Blackjack |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"\t\t\t\t\t\t\t|--- Runde: ----------------- {runde}")
            print(f"\t\t\t\t\t\t\t|--- Ihre Gewinne: ---------- {wins}")
            print(f"\t\t\t\t\t\t\t|--- Ihre Fehlschläge: ------ {losses}")
            print(f"\t\t\t\t\t\t\t|--- Ihre Black-Jacks: ------ {black_jacks}")
            print(f"\t\t\t\t\t\t\t|--- Ihr Geld: -------------- {money}")
            print(f"\t\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Blackjack |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\t\t\t\t\t\t\tSie haben auch jederzeit die Möglichkeit, mit [V] das Kasino zu verlassen")
            print("\n")
            print(f"Der aktuelle Blind:     {blind}")

            while blind_throw <= blind - 1 or blind_throw > money:
                blind_throw = int(input("Ihr Einsatz:\n\t"))
            money -= blind_throw

            while kartenwert < 100:
                kartenwert = 0

                if graphics_on_off != "on":
                    print("\n<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>\t\t\t\t\t")
                print(f"\nDeine Karten:", end="\t\t\t")

                for char in cards:
                    kartenwert += fnc_blackjack_werte.worth(char, graphics=graphics_on_off)

                    if graphics_on_off != "on":
                        print(char, end="; ")

                print(f"\n\nKartenwert:\t\t\t\t{kartenwert}\n")

                if graphics_on_off != "on":
                    print("<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>-<|>")

                if kartenwert == 21:
                    print("\nDu hast ein Blackjack!")
                    print("\nGewonnen!\n")
                    print(f'Sie bekommen "{blind_throw * 3}"€ ausgezahlt!\n')
                    wins += 1
                    black_jacks += 1
                    blind_throw = blind_throw * 3
                    money += blind_throw
                    break

                if kartenwert > 21:
                    print("\nSie haben verloren!")
                    if graphics_on_off == "on":
                        print("( ˘︹˘ )")
                    kartenwert = 100
                    losses += 1
                    break

                user = input("\n\nMoechten sie [Z]iehen, [K]lopfen oder [W]erfen?\n\t").lower()
                if user.lower() == "z":
                    cards.extend(random.choices(fnc_blackjack_werte.cards_list, k=1))
                elif user.lower() == "k":

                    while dealer_worth < 21:
                        print(f"Der Dealer zeiht eine Karte!")
                        print("\n")
                        dealer_card = random.choices(fnc_blackjack_werte.cards_list, k=1)
                        dealer_hand += dealer_card
                        dealer_worth += fnc_blackjack_werte.worth(dealer_card, graphics=graphics_on_off)
                        time.sleep(3)

                        if graphics_on_off != "on":
                            print(f"Die Karte ist:                                    {dealer_card}")
                        print(f"Zusammen ergeben seine Karten:                    {dealer_worth}\n")
                        time.sleep(3)

                        if dealer_worth > kartenwert and dealer_worth < 22:
                            print("\nDer Dealer hat sie überboten!")
                            print("Sie haben verloren!")
                            if graphics_on_off == "on":
                                print("( ˘︹˘ )")
                            losses += 1
                            ueberboten = True
                            break

                if ueberboten == True:
                    break

                elif dealer_worth > 21:
                    print("\nDer dealer hat verloren")
                    print("Sie haben gewonnen!")
                    print(f'Sie bekommen "{blind_throw * 2}"€ ausgezahlt!\n')
                    wins += 1
                    blind_throw = blind_throw * 2
                    money += blind_throw
                    break

                elif user.lower() == "w":
                    print("\nSie haben geworfen!")
                    print("Viel Glück bei der nächsten Runde!")
                    break

                elif user.lower() == "v":
                    print("\nSie haben das Kasino verlassen")
                    print("Wir wünschen ihnen noch einen schönen aufenthalt im Kasino")
                    print("Wenn sie wieder kommen, denken sie daran:\nGlücksspiel macht süchtig!")
                    exit()

            print("_____________________")
            print("Nächste Runde:")
            print("_____________________\n")
            break
