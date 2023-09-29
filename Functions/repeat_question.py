def repeat_question():
    frage = 1
    print("Do you want to play again?")
    while frage == 1:
        game = input("[Y]es or [N]o\n\t").lower()
        if "y" in game:
            # print("gueltige eingabe")
            print("\n")
            countinue = True
            return countinue
        elif "n" in game:
            # print("gueltige eingabe")
            print("Okay, good bye!")
            exit()
        else:
            # print("ungueltige eingabe")
            frage_2 = 1