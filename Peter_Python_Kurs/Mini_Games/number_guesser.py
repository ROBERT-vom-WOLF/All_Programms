import random
import fnc_ask_again
loop = 1
used_guesses = 0
game = 1
print("\t\t\t\t\t\t\t\tWillkommen beim Zahlen-Rate_Spiel\n\n")
schwierigkeit = int(input("Wähle deine Schwierigkeit:\t\t\t\t"))
guesses = int(input("Wähle deine Anzahl deiner Versuche:\t\t"))
while loop == 1:
    number = random.randint(0, schwierigkeit)
    while game == 1:
        answer = int(input("Dein guess:\t "))
        used_guesses += 1
        # print(number)
        if answer == number:
            print("Das ist sie")
            print("Glückwunsch!")
            print(f"In nur {used_guesses} Versuchen!")
            print("Respekt!")
        elif used_guesses == guesses:
            print("Nein, das ist es nicht")
            print("Du hast leider keine Versuche mehr")
            print(f"Die richtige Antwort war: {number}")
            print("Game Over")
        elif answer > number:
            print("Nein, das ist es nicht")
            print("Geh ein bisschen weiter runter")
            print('''
             |    |    |
            \./  \./  \./
            ''')
            print(f"Du hast noch {guesses - used_guesses} Versuche!\n")
        elif answer < number:
            print("Nein, das ist es nicht")
            print("Geh ein bisschen weiter hoch")
            print('''
            /'\  /'\  /'\ 
             |    |    |
            ''')
            print(f"Du hast noch {guesses - used_guesses} Versuche!\n")
        else:
            print("System:\tError")
    fnc_ask_again.play_again("play")
