import random as rnd
from fnc_uno_decks import cards_liste
kartenstapel = []


def give_card(count=1):
    global kartenstapel
    card_deck = []
    vzhsud = 0
    while vzhsud != count:
        card = rnd.choices(all_decks, k=1)
        for char2 in card:
            all_decks.remove(char2)
        card_deck.extend(card)
        vzhsud += 1
    return card_deck


class Player:
    cards = []
    move_log = []

    def __init__(self, karten):
        self.cards = karten


class Middle:
    middle_cards = []
    top_card = None


def game_prep(deck_ammount):
    global kartenstapel
    for _ in range(0, deck_ammount):
        print(range)
        all_decks.append(cards_liste)


me = Player(give_card(5))
you = Player(give_card(5))
game_prep(3)