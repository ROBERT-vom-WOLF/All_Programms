

cards_list = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

def worth(card, graphics="on"):
    if "Ace" in card:
        if graphics == "on":
            print('''
░█████╗░░█████╗░███████╗
██╔══██╗██╔══██╗██╔════╝
███████║██║░░╚═╝█████╗░░
██╔══██║██║░░██╗██╔══╝░░
██║░░██║╚█████╔╝███████╗
╚═╝░░╚═╝░╚════╝░╚══════╝
            ''', end="\n")
        card_worth = 11
        return card_worth
    if "King" in card:
        if graphics == "on":
            print('''
██╗░░██╗██╗███╗░░██╗░██████╗░
██║░██╔╝██║████╗░██║██╔════╝░
█████═╝░██║██╔██╗██║██║░░██╗░
██╔═██╗░██║██║╚████║██║░░╚██╗
██║░╚██╗██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░''', end="\n")
        card_worth = 10
        return card_worth
    if "Queen" in card:
        if graphics == "on":
            print('''
░██████╗░██╗░░░██╗███████╗███████╗███╗░░██╗
██╔═══██╗██║░░░██║██╔════╝██╔════╝████╗░██║
██║██╗██║██║░░░██║█████╗░░█████╗░░██╔██╗██║
╚██████╔╝██║░░░██║██╔══╝░░██╔══╝░░██║╚████║
░╚═██╔═╝░╚██████╔╝███████╗███████╗██║░╚███║
░░░╚═╝░░░░╚═════╝░╚══════╝╚══════╝╚═╝░░╚══╝''', end="\n")
        card_worth = 10
        return card_worth
    if "Jack" in card:
        if graphics == "on":
            print('''
░░░░░██╗░█████╗░░█████╗░██╗░░██╗
░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
░░░░░██║███████║██║░░╚═╝█████═╝░
██╗░░██║██╔══██║██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝''', end="\n")
        card_worth = 10
        return card_worth
    if "10" in card:
        if graphics == "on":
            print('''                
░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░██║░░██║
╚═╝██║░░██║░░██║
███████╗╚█████╔╝
╚══════╝░╚════╝░''', end="\n")
        card_worth = 10
        return card_worth
    if "9" in card:
        if graphics == "on":
            print('''           
░█████╗░
██╔══██╗
╚██████║
░╚═══██║
░█████╔╝
░╚════╝░''', end="\n")
        card_worth = 9
        return card_worth
    if "8" in card:
        if graphics == "on":
            print(''' 
░█████╗░
██╔══██╗
╚█████╔╝
██╔══██╗
╚█████╔╝
░╚════╝░''', end="\n")
        card_worth = 8
        return card_worth
    if "7" in card:
        if graphics == "on":
            print('''
███████╗
╚════██║
░░░░██╔╝
░░░██╔╝░
░░██╔╝░░
░░╚═╝░░░''', end="\n")
        card_worth = 7
        return card_worth
    if "6" in card:
        if graphics == "on":
            print('''
░█████╗░
██╔═══╝░
██████╗░
██╔══██╗
╚█████╔╝
░╚════╝░''', end="\n")
        card_worth = 6
        return card_worth
    if "5" in card:
        if graphics == "on":
            print('''
███████╗
██╔════╝
██████╗░
╚════██╗
██████╔╝
╚═════╝░''', end="\n")
        card_worth = 5
        return card_worth
    if "4" in card:
        if graphics == "on":
            print('''
░░██╗██╗
░██╔╝██║
██╔╝░██║
███████║
╚════██║
░░░░░╚═╝''', end="\n")
        card_worth = 4
        return card_worth
    if "3" in card:
        if graphics == "on":
            print('''
██████╗░
╚════██╗
░█████╔╝
░╚═══██╗
██████╔╝
╚═════╝░''', end="\n")
        card_worth = 3
        return card_worth
    if "2" in card:
        if graphics == "on":
            print('''
██████╗░
╚════██╗
░░███╔═╝
██╔══╝░░
███████╗
╚══════╝''', end="\n")
        card_worth = 2
        return card_worth
