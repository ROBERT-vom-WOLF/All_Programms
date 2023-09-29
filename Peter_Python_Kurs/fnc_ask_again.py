def play_again(Fragewort):
    frage = 1
    print(f"\nDo you want to {Fragewort} again?")
    while frage == 1:
        game = input("[Y]es or [N]o\n\t").lower()
        if "y" in game:
            # print("gueltige eingabe")
            print("\n")
            frage = 0
        elif "n" in game:
            print("Okay, good bye!")
            exit()
        else:
            print('please answer with "y" for Yes or "n" for No')