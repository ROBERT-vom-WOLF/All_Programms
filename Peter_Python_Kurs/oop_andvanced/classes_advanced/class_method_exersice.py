import random as rnd


class Card:
    all_colors = ["Kreuz", "Herz", "Pik", "Karo"]
    all_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

    def __init__(self, wert, farbe):
        self.color = farbe
        self.value = wert

    def __repr__(self):
        output = f'''
        Value:\t{self.value}
        Color:\t{self.color}'''
        return output

    def get_colors(self):
        return self.all_colors

    def get_values(self):
        return self.all_values


class Deck:
    all_cards = []

    def __init__(self):
        for color in Card.all_colors:
            for value in Card.all_values:
                self.all_cards.append(f"{color} {value}")

    def __repr__(self):
        output = ""
        num = 0
        for x in self.all_cards:
            num += 1
            output += f"{num}:\t{x}\n"

        return output

    def mix(self):
        rnd.shuffle(self.all_cards)

    def count(self):
        return len(self.all_cards)

    def give_multiple(self, ammount=1):
        given_cards = self.all_cards[0:ammount]
        self.all_cards.remove(given_cards)
        return given_cards

    def give(self, ammount=1):
        if len(self.all_cards) > 0:
            given_card = self.all_cards[0:ammount]
            self.all_cards.remove(given_card)
            return given_card


karte = Card(2, "herz")
stapel = Deck()
print(stapel)
