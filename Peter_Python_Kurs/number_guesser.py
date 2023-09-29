import random
import fnc_ask_again
loop = 1
used_guesses = 0
game = 1
print("\t\t\t\t\t\t\t\tWillkommen beim Zahlen-Rate_Spiel\n\n")
schwierigkeit = int(input("Wähle deine Schwierigkeit:\t\t\t\t"))
guesses = int(input("Wähle deine Anzahl deiner Versuche:\t\t"))
while loop == 1:
    while game == 1:
        number = random.randint(0, schwierigkeit)
        answer = int(input("Deine Annahme:\t "))
        used_guesses += 1
        if used_guesses == guesses:
            print("Du hast keine Versuche Mehr")
            print("Game Over")
        elif answer == number:
            print("Das ist sie")
            print("Glückwunsch!")
            print(f"In nur {used_guesses} Versuchen!")
            print("Respekt!")
        elif answer > number:
            print("Nein, das ist es nicht")
            print("Geh ein bisschen weiter runter")
            print(f"Du hast noch {guesses - used_guesses} Versuche!\n")
        elif answer < number:
            print("Nein, das ist es nicht")
            print("Geh ein bisschen weiter hoch")
            print(f"Du hast noch {guesses - used_guesses} Versuche!\n")
        else:
            print("System:\tError")
    fnc_ask_again.play_again("play")
