def ask(Fragewort, Language="EN"):
    frage = 1
    if Language == "DE":
        print(f"\nMoechten sie nochmals {Fragewort}?")
        while frage == 1:
            game = input("[J]a oder [N]ein\n\t").lower()
            if "j" in game:
                # print("gueltige eingabe")
                print("\n")
                frage = 0
            elif "n" in game:
                print("Okay, schoenen Tag!")
                exit()
            else:
                print('Bitte Antworte nur mit "J" fuer Ja oder "N" fuer Nein.')
    elif Language == "EN":
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
