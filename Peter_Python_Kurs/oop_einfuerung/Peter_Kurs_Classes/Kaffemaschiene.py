from Kaffemaschine_dicts import *
import time as t


def concole_infos():
    print("Kaffemaschine\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tmade by Robert")
    print("\n\nCommands:")
    print('\t\t"-help"\t\t\tGibt diese Liste von befehlen erneut aus')
    print('\t\t"-quit"\t\t\tProgramm beenden')
    print('\t\t"-stop"\t\t\tBezahlung abbrechen (nur möglich während des Bezahlvorgangs!)')
    print('\t\t"-info"\t\t\tDetails zu einem Kaffe\t(bsp: espresso -info)')
    print('\t\t"-refill"\t\tStockt die Vorräte der Kaffee-Maschiene wieder auf')
    print('\t\t"-status"\t\tZeigt inhalt der Maschiene an')
    print('\n\t\tTIPP:\t\t\tDer anfangsbuchstabe des Kaffee`s ist ausreichend!\t(bsp: espresso = e)')
    print("\n")


def commands(user):
    used_commands = 0
    if "-quit" in user:
        exit()

    if "-help" in user:
        concole_infos()

    if "-info" in user:
        print("\n------Kaffe Infos:")
        print(f"Preis:\t\t{kaffe.preis}")
        print(f"Bohnen:\t\t{kaffe.bohnen_kosten}")
        print(f"Wasser:\t\t{kaffe.wasser_kosten}")
        print(f"Milch:\t\t{kaffe.milch_kosten}")
        print("------------------------\n\n")
        used_commands += 1

    if "-refill" in user:
        Resources.wasser_vorrat = resources["water"]
        Resources.milch_vorrat = resources["milk"]
        Resources.bohnen_vorrat = resources["coffee"]
        Resources.geld_vorrat = resources["money"]
        print("Die Kaffee-Maschiene wurde wieder befüllt!\n")
        user = "-status"     # nach dem refill wird der Status somit automatisch ausgegeben
        used_commands += 1

    if "-status" in user:
        print("\n------Maschienen-Status:")
        print(f"Laufzeit:\t{round(t.time() - start)}s")
        print(f"Bohnen:\t\t{maschiene.bohnen_vorrat}")
        print(f"Wasser:\t\t{maschiene.wasser_vorrat}")
        print(f"Milch:\t\t{maschiene.milch_vorrat}")
        print(f"Geld:\t\t{maschiene.geld_vorrat}")
        print("------------------------\n\n")
        used_commands += 1

    if used_commands > 0:
        return True
    else:
        return False


class Kaffee:
    preis = 0
    wasser_kosten = 0
    bohnen_kosten = 0
    milch_kosten = 0
    chosen_kaffee = "None"

    def __init__(self, eingabe):
        if eingabe[0] == "e":
            self.chosen_kaffee = "e"
            self.preis = MENU["espresso"]["cost"]
            self.wasser_kosten = MENU["espresso"]["ingredients"]["water"]
            self.bohnen_kosten = MENU["espresso"]["ingredients"]["coffee"]
            self.milch_kosten = 0

        elif eingabe[0] == "l":
            self.chosen_kaffee = "l"
            self.preis = MENU["latte"]["cost"]
            self.wasser_kosten = MENU["latte"]["ingredients"]["water"]
            self.bohnen_kosten = MENU["latte"]["ingredients"]["coffee"]
            self.milch_kosten = MENU["latte"]["ingredients"]["milk"]

        elif eingabe[0] == "c":
            self.chosen_kaffee = "c"
            self.preis = MENU["cappuccino"]["cost"]
            self.wasser_kosten = MENU["cappuccino"]["ingredients"]["water"]
            self.bohnen_kosten = MENU["cappuccino"]["ingredients"]["coffee"]
            self.milch_kosten = MENU["cappuccino"]["ingredients"]["milk"]

        else:
            self.chosen_kaffee = "None"
            print("ungueltige eingabe für einen Kaffe!\n")
            self.milch_kosten = 0
            self.bohnen_kosten = 0
            self.wasser_kosten = 0
            self.preis = 0


class Resources:
    wasser_vorrat = resources["water"]
    milch_vorrat = resources["milk"]
    bohnen_vorrat = resources["coffee"]
    geld_vorrat = resources["money"]


def bezahlen(preis):
    while True:
        print(f"Kosten: {preis}")
        print("Ihre Einzahlung:")
        quarters = input("Quarters(0,25 $):    ")
        dimes = input("Dimes(0,10 $):       ")
        nickles = input("Nickles(0,05 $):     ")
        pennys = input("Pennys(0,01 $):      ")

        if "-stop" in quarters or "-stop" in dimes or "-stop" in nickles or "-stop" in pennys:
            print("Zahlvorgang abgebrochen!\n\n")
            return
        else:
            eingezahlt = int(quarters) * 0.25
            eingezahlt += int(dimes) * 0.10
            eingezahlt += int(nickles) * 0.05
            eingezahlt += int(pennys) * 0.01
            if eingezahlt < preis:
                print("\nUngenügend Geld eingezahlt!")
                print(f"Es fehlt ihnen {preis - eingezahlt} $\n")

            elif eingezahlt > preis:
                print(f"Sie bekommen {eingezahlt - preis} $ zurrück!")
                print("`nen guten!")

            elif eingezahlt == preis:
                print("Passende Einzahlung!")
                Resources.milch_vorrat -= kaffe.milch_kosten
                Resources.wasser_vorrat -= kaffe.wasser_kosten
                Resources.bohnen_vorrat -= kaffe.bohnen_kosten
                Resources.geld_vorrat += kaffe.preis
                print("`nen guten!")
                return


def accessable(wasser, milch, bohnen):
    if Resources.wasser_vorrat - wasser <= 0:
        print("Ungenügend Wasser!")
        return False
    elif Resources.bohnen_vorrat - bohnen <= 0:
        print("Ungenügend Bohnen!")
        return False
    elif Resources.milch_vorrat - milch <= 0:
        print("Ungenügend Milch!")
        return False
    else:
        return True


concole_infos()
maschiene = Resources
start = t.time()
while True:
    user_input = input("[E]spresso?, [L]atte oder [C]appuccino?\t").lower().strip()
    if user_input[0] == "e" or user_input[0] == "l" or user_input[0] == "c" or user_input[0] == "-":
        kaffe = Kaffee(user_input)
        command_used = commands(user_input)
        if accessable(kaffe.wasser_kosten, kaffe.milch_kosten, kaffe.bohnen_kosten) and not command_used:
            bezahlen(kaffe.preis)
    else:
        print("Keine Gültige Eingabe!\n")
