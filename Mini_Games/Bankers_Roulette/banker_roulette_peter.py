import random
import fnc_ask_again
loop = 1
while loop == 1:
    print("Wer soll heute zahlen?")
    print('Bitte beachten sie, dass sie alle Personen mit einem Leerzeichen trennen.\n ')
    eingabe = input("Namen:\t")
    names = eingabe.split(" ")
    zahler = random.choices(names)
    zahler_str = str(zahler)
    letters = zahler_str.count("")
    zahler_str = zahler_str[2:(letters - 3)]
    print(f"Es ist: {zahler_str}")
    fnc_ask_again.ask("einen zahlenen bestimmen", "DE")
