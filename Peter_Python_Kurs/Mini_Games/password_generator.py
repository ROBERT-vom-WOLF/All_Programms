import random
from fnc_ask_again import *
while True:
    stellen = 0
    password = []
    numbers_list = ["0", "1", "2", "3", "4", "5", "6" "7", "8", "9"]
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                     "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":",
                   ",", ".", "<", ">", "/", "?", "|", "\\", "~", "`", "'", "\"", "§", "©", "®", "™", "€", "¥", "£", "¢",
                   "¤", "µ", "°", "¬", "¦", "§", "±", "²", "³", "¼", "½", "¾"]
    abc_request = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\tPassword_Generator\nGewünschte Anzahl der Buchstaben:\t"))
    numbers_request = int(input("Gewünschte Anzahl der Zahlen:\t"))
    symbols_request = int(input("Gewünschte Anzahl der Zeichen:\t"))
    abc = random.choices(alphabet_list, k=abc_request)
    numbers = random.choices(numbers_list, k=numbers_request)
    symbols = random.choices(symbol_list, k=symbols_request)
    password.extend(abc)
    password.extend(numbers)
    password.extend(symbols)
    random.shuffle(password)
    print("Passwort:\n\t")
    for char in password:
        print(char, end="")
        stellen += 1
    print(f"\nDas Passwort hat {stellen} Stellen.")
    print("\n\n")
    print("_____________________________________________________")
    ask("generieren", "DE")

