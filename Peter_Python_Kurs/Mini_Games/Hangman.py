import random
from hangman_art import *
import fnc_ask_again
possible_words = ["Haus", "Auto", "Katze", "Hund", "Tisch", "Stuhl", "Buch", "Blume", "Garten", "Sonne", "Mond", "Sterne", "Schule", "Lehrer", "Schüler", "Kaffee", "Tee", "Wasser", "Feuer", "Erde", "Luft", "Musik", "Film", "Theater", "Stadt", "Land", "Telefon", "Computer", "Brot", "Butter", "Käse", "Obst", "Gemüse", "Sommer", "Herbst", "Winter", "Frühling", "Familie", "Freunde", "Liebe", "Glück", "Traurigkeit", "Angst", "Freiheit", "Reisen", "Abenteuer", "Lachen", "Weinen", "Sport", "Musik", "Kunst", "Farben", "Essen", "Trinken", "Schlafen", "Lesen", "Schreiben", "Spielen", "Lernen", "Entspannen", "Elefant", "Buchstabe", "Universum", "Geburtstag", "Wunderbar", "Schokolade", "Abenteuer", "Telefonat", "Apotheker", "Fantastisch"]
weiter = 1

while weiter == 1:
    versuche = 7
    word = random.choice(possible_words)
    word = str(word)
    word = word.lower()
    answer = ""
    game = 0
    print(word)
    print(logo)
    while versuche > 0:
        game = 0
        for char in word.lower():
            if char in answer:
                print(char, end=""),
            else:
                print(" _ ", end=""),
                game += 1
        print(stages[versuche - 1])
        if game == 0:
            print("\nDu hast gewonnen!")
            versuche = 0
        user = input("\tDein Buchstabe\t").lower()
        answer = user + answer
        if user.lower() not in word.lower():
            versuche -= 1
            print("Falsch!")
            if versuche == 0:
                print(f"Du hast keine versuche mehr!")
                print(f"Die richtige Antwort war: {word}")
                print("Game Over")
            else:
                print(f"Du hast noch {versuche} Versuche!")
    fnc_ask_again.ask("spielen", "DE")

# letters = word.count("")
# stellen = []
# durchgang = 1
#
#     while letters > durchgang:
#         stellen = stellen + ["_"]
#         durchgang += 1
#     print(stellen)
#     user = input("Dein Buchstabe\t").lower()
#     user = str(user)
#     stellenwert = word.find(user) + 1
#     if stellen[stellenwert - 1] == stellen[stellenwert - 1]:
#         stellenwert = word.find(user) + stellenwert
#     if stellenwert >= 1:
#         print("Das ist richtig\n")
#         stellen[stellenwert - 1] = user
#
#     elif stellenwert <= 0:
#         print("Falsch!")
#         versuche -= 1
#         print(f"Du hast noch {versuche} versuch(e)!\n")
#
#     else:
#         print("System\tError")
#         exit()
# if versuche == 0:
#     print("Keine Versuche mehr!")
#     print(f"Das gesuchte Wort war: {word}")
#     print("Game Over")
#     exit()
