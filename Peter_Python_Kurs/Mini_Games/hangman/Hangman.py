import random
import time
from hangman_art import *
from symbols_n_words import *
import fnc_ask_again
while True:
    word = random.choice(german_words)
    used_letters = ""
    versuche = 7
    answer = ""
    game = 0
    user = ""
    print(logo)
    letters_request = 0
    while letters_request <= 1:
        letters_request = int(input("Wie viele Zeichen darf das Wort maximal haben?\t"))
    while len(word) > letters_request:
        word = random.choice(german_words)
    word_stellen = len(word)
    while versuche > 0:
        user = ""
        game = 0
        print("\n\t")
        for char in word.upper():
            if char in answer:
                print(char, end="")
            else:
                print(" _ ", end="")
                game += 1
        print(f"\t({word_stellen} Stellen)\n\n")
        if user.upper() == word.lower():
            print("\nDu hast gewonnen!")
            versuche = 0
            fnc_ask_again.ask("spielen", "DE")
        elif game == 0:
            print("\nDu hast gewonnen!")
            versuche = 0
        if versuche > 0:
            while user[0:1] not in alphabet_list:
                user = input("Dein Buchstabe:\n\t").upper()
            answer = user + answer
            print(f"Trommelwirbel!!")
            print(f'Dein Buchstabe " {user} " ist...')
            time.sleep(0.7)
        if user not in word.upper():
            versuche -= 1
            print("\n\t\t\t\tFalsch!")
            print(f"{stages[versuche]}")
            used_letters += user + "  "
            if versuche == 0:
                print(f"Du hast keine versuche mehr!")
                print(f"Die richtige Antwort war\t\t {word}")
                print("\t\tGame Over")
        else:
            print("Richtig!")
        time.sleep(0.8)
        if versuche > 0:
            print(f"\t\t\t\t\t\t\t____________________________________| HANGMAN |____________________________________")
            print(f"\t\t\t\t\t\t\tDeine falschen Buchstaben:\t\t{used_letters.upper()}")
            print(f"\t\t\t\t\t\t\tDeine verbleibenden Versuche:\t{versuche}")
            print(f"\t\t\t\t\t\t\t____________________________________| ======= |____________________________________")
        if versuche == 0:
            fnc_ask_again.ask("spielen", "DE")
        time.sleep(0.8)
