import random
import time
from hangman_art import *
from hangman_words import *
import fnc_ask_again
weiter = 1
while weiter == 1:
    word = random.choice(german_words)
    used_letters = []
    versuche = 7
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
            user = input("\n\nDein Buchstabe:\n\t").lower()
            answer = user + answer
            print(f"Trommelwirbel!!")
            print(f'Dein Buchstabe " {user} " ist...')
            time.sleep(1.5)

        if user.lower() not in word.lower():
            versuche -= 1
            print("Falsch!")
            used_letters += user.lower()
            if versuche == 0:
                print(f"Du hast keine versuche mehr!")
                print(f"Die richtige Antwort war\t\t {word}")
                print("\t\tGame Over")
        else:
            print("Richtig!")

        if versuche <= 6:
            print(stages[versuche])
            time.sleep(0.5)
        time.sleep(0.2)
        if versuche > 0:
            print("______________________________________________________________________________")
            print(f"Deine falschen Buchstaben: {used_letters}")
            print(f"Deine verbleibenden Versuche: {versuche}")
            print("______________________________________________________________________________")
        time.sleep(0.2)
        if versuche == 0:
            fnc_ask_again.ask("spielen", "DE")
