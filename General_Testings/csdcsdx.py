import random
cards_list = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
card_list_numbers = [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
card = random.choices(cards_list, weights=[10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
card_str = str(card)
print(card)
while card_list_numbers[cards_list.index(card_str[2:5])] >= 4:
    card = random.choice(cards_list)
    card_stelle = cards_list.index(card)
card_list_numbers[card_stelle] += 1
print(card)
print(card_stelle)
print(card_list_numbers)
