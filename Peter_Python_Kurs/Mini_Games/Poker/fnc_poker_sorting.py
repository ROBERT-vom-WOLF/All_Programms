from fnc_poker_cards import card_list
import random as rnd


def poker_sort_all_cards(player_1_cards, player_2_cards, player_3_cards, player_4_cards, player_5_cards, open_cards):
    all_cards = []
    all_cards += player_5_cards + player_4_cards + player_4_cards + player_3_cards + player_2_cards + player_1_cards + open_cards
    all_cards = sorted(all_cards, key=lambda k: k[9:10], reverse=True)
    return list(all_cards)


def poker_sort_player_cards(player_1_cards, player_2_cards, player_3_cards, player_4_cards, player_5_cards):
    all_player_cards = []
    all_player_cards += player_5_cards + player_4_cards + player_4_cards + player_3_cards + player_2_cards + player_1_cards
    all_player_cards = sorted(all_player_cards, key=lambda k: k[9:10], reverse=True)
    return list(all_player_cards)


def wothing(list):
    wothing_list = []
    for card in list:
        if card[9:10] == "A":
            wothing_list.extend(card[9:10])
            return 11

        elif card[9:10] == "K":
            wothing_list.extend(card[9:10])
            return 10

        elif card[9:10] == "Q":
            wothing_list.extend(card[9:10])
            return 10

        elif card[9:10] == "J":
            wothing_list.extend(card[9:10])
            return 10

        elif card[9:10] == "T":
            wothing_list.extend(card[9:10])
            return 10

        elif card[9:10] == "9":
            wothing_list.extend(card[9:10])
            return 9

        elif card[9:10] == "8":
            wothing_list.extend(card[9:10])
            return 8

        elif card[9:10] == "7":
            wothing_list.extend(card[9:10])
            return 7

        elif card[9:10] == "6":
            wothing_list.extend(card[9:10])
            return 6

        elif card[9:10] == "5":
            wothing_list.extend(card[9:10])
            return 5

        elif card[9:10] == "4":
            wothing_list.extend(card[9:10])
            return 4

        elif card[9:10] == "3":
            wothing_list.extend(card[9:10])
            return 3

        elif card[9:10] == "2":
            wothing_list.extend(card[9:10])
            return 2


player_1_cards = rnd.choices(card_list, k=2)
player_2_cards = rnd.choices(card_list, k=2)
player_3_cards = rnd.choices(card_list, k=2)
player_4_cards = rnd.choices(card_list, k=2)
player_5_cards = rnd.choices(card_list, k=2)
open_cards = rnd.choices(card_list, k=5)

# poker_sort(player_1_cards, player_2_cards, player_3_cards, player_4_cards, player_5_cards, open_cards)
# player_5_cards = sorted(player_5_cards, key=lambda k: k[9:10], reverse=True)
# print(player_5_cards)

cards = []
# print(poker_sort_player_cards(player_1_cards, player_2_cards, player_3_cards, player_4_cards, player_5_cards))
cards.extend(poker_sort_all_cards(player_1_cards, player_2_cards, player_3_cards, player_4_cards, player_5_cards, open_cards))

print(wothing(cards))


def poker_sort(card):
    all_cards = []
    all_cards += player_5_cards + player_4_cards + player_4_cards + player_3_cards + player_2_cards + player_1_cards + open_cards
    all_cards = sorted(all_cards, key=lambda k: k[9:10], reverse=True)
    return list(all_cards)
