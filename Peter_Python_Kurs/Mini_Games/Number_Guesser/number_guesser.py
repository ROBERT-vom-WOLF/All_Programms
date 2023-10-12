import random
import fnc_ask_again
used_guesses = 0
print("\t\t\t\t\t\t\t\tWillkommen beim Zahlen-Rate_Spiel\n\n")
schwierigkeit = int(input("Wähle deine Schwierigkeit:\t\t\t\t"))
guesses = int(input("Wähle deine Anzahl deiner Versuche:\t\t"))
while True:
    number = random.randint(0, schwierigkeit)
    while True:
        answer = int(input("Dein guess:\t "))
        used_guesses += 1
        if answer > schwierigkeit:
            print('''
            
            Du bist ueber deinem eigen festgelegten Maximum!
            ''')
        if answer == number:
            print("Das ist sie")
            print("Glückwunsch!")
            print(f"In nur {used_guesses} Versuchen!")
            print("Respekt!")
            break
        elif used_guesses == guesses:
            print("Nein, das ist es nicht")
            print("Du hast leider keine Versuche mehr")
            print(f"Die richtige Antwort war: {number}")
            print("Game Over")
            break
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
    fnc_ask_again.ask("spielen", "DE")
