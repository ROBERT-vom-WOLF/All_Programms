

cards_list = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]


# def list():
#     cards_list = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#     card_list_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     card = random.choice(cards_list)
#     print(cards_list.index(card))


def worth(card):
    if "Ace" in card:
        card_worth = 11
        return card_worth
    if "King" in card or "Queen" in card or "Jack" in card:
        card_worth = 10
        return card_worth
    if "10" in card:
        card_worth = 10
        return card_worth
    if "9" in card:
        card_worth = 9
        return card_worth
    if "8" in card:
        card_worth = 8
        return card_worth
    if "7" in card:
        card_worth = 7
        return card_worth
    if "6" in card:
        card_worth = 6
        return card_worth
    if "5" in card:
        card_worth = 5
        return card_worth
    if "4" in card:
        card_worth = 4
        return card_worth
    if "3" in card:
        card_worth = 3
        return card_worth
    if "2" in card:
        card_worth = 2
        return card_worth
