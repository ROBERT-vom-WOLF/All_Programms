import random
loop = 1
frage = 1
draws = 0
wins = 0
losses = 0
answer = ""
print("Hey You!!")
print("Lets Play a Game!")

while loop == 1:
    frage = 1
    while frage == 1:
        answer = input('[R]ock, [P]aper, [S]issors]!\n\t').lower()
        if "r" in answer or "p" in answer or "s" in answer:
            # print("gueltige eingabe")
            frage = 0
        elif "r" not in answer or "p" not in answer or "s" not in answer:
            # print("ungueltige eingabe")
            frage = 1
    print("\n")
    zeichen = random.randint(1, 3)
    if zeichen == 1:
        if "r" in answer.lower():
            print("Your opponent showed Rock!")
            print("Draw.")
            frage = 0
            draws += 1
        if "p" in answer.lower():
            print("Your opponent showed Rock!")
            print("You won!")
            frage = 0
            wins += 1
        if "s" in answer.lower():
            print("Your opponent showed Rock!")
            print("You lost!")
            frage = 0
            losses += 1
    elif zeichen == 2:
        if "p" in answer.lower():
            print("Your opponent showed Paper!")
            print("Draw.")
            frage = 0
            draws += 1
        if "s" in answer.lower():
            print("Your opponent showed Paper!")
            print("You won!")
            frage = 0
            wins += 1
        if "r" in answer.lower():
            print("Your opponent showed Paper!")
            print("You lost!")
            frage = 0
            losses += 1
    elif zeichen == 3:
        if "s" in answer.lower():
            print("Your opponent showed Sissor!")
            print("Draw.")
            frage = 0
            draws += 1
        if "r" in answer.lower():
            print("Your opponent showed Sissor!")
            print("You won!")
            frage = 0
            wins += 1
        if "p" in answer.lower():
            print("Your opponent showed Sissor!")
            print("You lost!")
            frage = 0
            losses += 1
    if "r" in answer or "p" in answer or "s" in answer:
        print("\n\t\t\t___________________________________________")
        print("\t\t\tYour statistics:")
        print(f"\t\t\tWins: \t\t{wins}")
        print(f"\t\t\tLosses: \t{losses}")
        print(f"\t\t\tDraws: \t\t{draws}")
        print("\t\t\t___________________________________________")

    print("Do you want to play again?")
    game = input("[Y]es or [N]o\n\t").lower()
    if "y" in game:
        loop = 1
    else:
        loop = 0
        print("Okay, good bye!")
        exit()
