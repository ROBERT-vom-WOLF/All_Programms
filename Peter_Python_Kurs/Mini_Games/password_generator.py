import random
import time
import fnc_ask_again
while True:
    wait_count = ""
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
    wait_time = len(password)
    print(f"Password wird generiert")
    print(". ", end="")
    time.sleep(0.35)
    print(". ", end="")
    time.sleep(0.35)
    print(". ", end="")
    time.sleep(0.35)
    print("\n\t\t\t\t_________________________________________________________________________________________________")
    print("\t\t\t\tPasswort:\t\t\t\t", end="")
    for char in password:
        print(char, end="")
        stellen += 1
    print(f"\n\t\t\t\tStellen:\t\t\t\t{stellen}")
    print("\t\t\t\t_________________________________________________________________________________________________\n")
    if stellen >= 100:
        print("Das Passwort ist extrem sicher!")
    elif stellen >= 50:
        print("Das Passwort ist sicher!")
    elif stellen >= 20:
        print("Das Passwort ist funktional, doch es werden mehr zeichen Empfohlen!")
    else:
        print("Das Passwort ist nicht sicher! Verwenden sie mehr Zeichen, um es sicherer zu machen!")
    print("\n")
    print("_____________________________________________________")
    fnc_ask_again.ask("generieren", "DE")
