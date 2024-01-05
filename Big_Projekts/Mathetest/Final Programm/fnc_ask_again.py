def ask(Fragewort, Language="EN"):
    if Language == "DE":
        print(f"\nMoechtest du weiter {Fragewort}?")
        while True:
            game = input("[J]a oder [N]ein\n\t").lower()
            if "j" in game:
                print("\n")
                break
            elif "n" in game:
                print("Okay, schoenen Tag!")
                exit()
            else:
                print('Bitte Antworte nur mit "J" fuer Ja oder "N" fuer Nein.')
    elif Language == "EN":
        print(f"\nDo you want to {Fragewort} again?")
        while True:
            game = input("[Y]es or [N]o\n\t").lower()
            if "y" in game:
                # print("gueltige eingabe")
                print("\n")
                break
            elif "n" in game:
                print("Okay, good bye!")
                exit()
            else:
                print('please answer with "y" for Yes or "n" for No')
