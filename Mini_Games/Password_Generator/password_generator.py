import random
import time
from symbols_n_words import *
from fnc_ask_again import *
while True:
    stellen = 0
    password = []
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
    print(f"Passwort wird generiert")
    time.sleep(0.5)
    print(". ", end="")
    time.sleep(0.35)
    print(". ", end="")
    time.sleep(0.35)
    print(". ", end="")
    time.sleep(0.35)

    while True:
        print("\n")
        stellen += 1
        if stellen > 30:
            break
    stellen = 0

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
    ask("generieren", "DE")
