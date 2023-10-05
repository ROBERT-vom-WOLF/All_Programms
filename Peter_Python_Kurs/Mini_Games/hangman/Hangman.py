import random
from hangman_art import *
from hangman_words import *
import fnc_ask_again
weiter = 1
while weiter == 1:
    versuche = 7
    word = random.choice(german_words)
    answer = ""
    game = 0
    user = ""
    print(logo)
    while versuche > 0:
        game = 0
        print("\n")
        for char in word.lower():
            if char in answer:
                print(char, end=""),
            else:
                print(" _ ", end=""),
                game += 1
        if user.lower() == word.lower():
            print("\nDu hast gewonnen!")
            versuche = 0
            fnc_ask_again.ask("spielen", "DE")
        elif game == 0:
            print("\nDu hast gewonnen!")
            versuche = 0
        if versuche > 0:
            user = input("\n\nDein Buchstabe\n").lower()
            answer = user + answer
        if user.lower() not in word.lower():
            versuche -= 1
            print("Falsch!")
            if versuche == 0:
                print(f"Du hast keine versuche mehr!")
                print(f"Die richtige Antwort war: {word}")
                print("\t\t\tGame Over")
            else:
                print(f"Du hast noch {versuche} Versuch(e)!")
        if versuche == 0:
            fnc_ask_again.ask("spielen", "DE")
        else:
            print(stages[versuche])
