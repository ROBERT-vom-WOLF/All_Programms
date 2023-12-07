import random
from side_functions import *
kartenstapel = []


def give_card(count_request=1):
    global kartenstapel
    card_deck = []
    for _ in range(0, count_request):
        cards = random.choices(kartenstapel, k=1)
        for char in cards:
            kartenstapel.remove(char)
            card_deck.append(char)
    return card_deck


class Player:
    cards = []                      # die Karten / Hand des Spielers. Wird immer mit 'sorted()' ausgegeben!
    move_log = []                   # ein log der getätigten Aktionen bsp: ["karte ziehen", "Blue 3", ...]
    skipped = False                 # für die aussetzen- und richtungswechsel-Karten
    color = None                    # für die Wunschfunktion der +4 karte
    add_on_cards = [x for x in cards if "+" == x[8:9]]

    def __init__(self, karten):
        self.cards = sorted(karten)

    def change_skipped_status(self):
        if self.skipped:
            self.skipped = False
        else:
            self.skipped = True

    def move(self):
        user = int(input("Du legst:\t")) - 1
        self.move_log.append(f"{self.cards[user]}")
        self.cards.remove(self.cards[user])

    def color_pick(self):                                   # funktion zum ändern der Farbpriorität
        print("Welche Farbe möchtest du?")
        while True:
            user_1 = input("[B]lue, [R]ed, [Y]ellow oder [G]reen?\t").lower().replace(" ", "")

            if user_1 == "b" or user_1 == "blue":
                self.color = "blue"
                break
            if user_1 == "y" or user_1 == "yellow":
                self.color = "yellow"
                break
            if user_1 == "g" or user_1 == "green":
                self.color = "green"
                break
            if user_1 == "r" or user_1 == "red":
                self.color = "red"
                break


def game_prep(deck_ammount):
    global kartenstapel
    for _ in range(0, deck_ammount):
        kartenstapel.extend(cards_liste)


def show_stats(player_class, upper_card, cards=False, log=False, show_all=False):
    if cards or show_all:
        print(f"Spieler {player_list.index(player_class) + 1}")
        print(f"Oberste Karte:\t\t", end="")
        for char in upper_card:
            print(char)
        print(f"Deine Karten:")
        num = 0
        for char in player_class.cards:
            num += 1
            print(f"{num}:\t{char}")
        print("\n")
    if log or show_all:
        print(f"Player Log: {player_class.move_log}")


middle_cards = []               # der mittlere Kartenstapel auf den alle ihre Karten legen
reversed_status = False         # noch unwichtig, nur wichtig für das nachfolger Programm mit mehr Spielern
game_prep(1)
player_list = []
player_count = int(input("Spieleranzahlt: "))
for _ in range(0, player_count):
    player_list.append(Player(give_card(5)))
all_used_cards = [random.choices(kartenstapel)]

while True:
    for current_player in player_list:
        top_card = all_used_cards[-1]       # die oberste Karte, wird mit 'middle_cards[-1]' definiert
        show_stats(current_player, top_card, show_all=True)
        print(f"Plus Karten: {current_player.add_on_cards}")
        current_player.move()
        show_stats(current_player, top_card, show_all=True)
        input("next round ----->")
    print("\n\nque restart...\n\n")

# DONE: Alle Spieler werden in einer Liste gespeichert und einzeln durchgegangen, das ermöglicht viele Spieler
# TODO: Die Spielrichtung kann mit [::-1] und [::1] geändert werden
# TODO: Karten nur legen können, wenn es erlaubt ist
# TODO: Karten Legen können + wenn man nicht legen kann eine nachziehen
# TODO: Nachgezogen darf nur werden, wenn es keine andere Option gibt
# TODO: Nach dem Nachziehen darf man (falls möglich) nochmal legen, aber nicht nachziehen
# TODO: Funktion von +2 / +4 Karten
# TODO: +2 / +4 Karten erweitern erst deine Hand, wenn du nicht mehr erhöhen kannst
# TODO: Falls du erhöhen kannst, darfst du entscheiden, ob du erhöst oder aufnimmst
# TODO: Zeige immer an, wie viel man bei einer Pluskarte aufnehmen muss. zählt mit den erhöhungen mit
# TODO: Command zum aufgeben einbauen
# TODO: wechsel-Funktion zwischen den einzelnen spielern mit zeilenumbrüchen und Timer
# TODO:
# TODO:
# TODO: (letztes) Funktion erstellen, um den input wiederholt nachzufragen, bis die eingabe möglich ist
