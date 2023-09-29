import random
schwierigkeit = 30
score_goal = 50
zeichen = 3
Joker = 1
score = 0
game = 1


def einleitung_1():
    global schwierigkeit
    print("\t\t\t\t\tMathematik Test\n\n")
    print("Bitte gebe eine beliebige Zahlen an.\nUm so hoeher, um so schwerer wird der Test.")
    schwierigkeit = int(input("\t"))
    return schwierigkeit


def einleitung_2():
    global score_goal
    print('Dieses Spiel zaehlt mit, wie viele Fragen du infolge richtig hattest.\nDas ist der sogenannte "Score".')
    print('Dein "Score Goal" ist dein erwuenschter "Score". Dann wird das spiel pausiert\n')
    score_goal = int(input('Welchen "Score" moechtest du heute erreichen? Wir empfehlen 50\n\t'))
    print("\nGut, dann lass uns jetzt anfangen!")
    print("\nBitte achte darauf, das du keine anderen Zeichen, außer deiner Antwortzahlen verwendest!")
    print("___________________________________________________________________________________________________________")
    return score_goal


def game_loop():
    global game
    global schwierigkeit
    global score_goal
    global zeichen
    global Joker
    global score
    nummer_1 = random.randint(1, schwierigkeit)
    nummer_2 = random.randint(1, schwierigkeit)
    devide_if = random.randint(1, 4)
    devide_else = random.randint(1, 3)
    str(nummer_1)
    str(nummer_2)
    if devide_if == 4:
        if nummer_1 % nummer_2 == 0:
            zeichen = devide_if
        else:
            zeichen = devide_else
    if score == score_goal:
        print("Du hast dein Score Goal errreicht! Glueckwunsch!")
        print("Moechtest du noch weiter machen?")
        farge_weiter = input('Antworte mit "ja"" oder "nein"\n\t')

        if farge_weiter.lower() == 'ja':
            zusaetzlicher_score = int(input("Um wie viel moechtest du dein Score Goal erhoehen?\n\t"))
            score_goal = score_goal + zusaetzlicher_score

        else:
            print("Schade, das du aufhoerst.")
            exit()
    if zeichen == 1:
        right_answer = int(nummer_1 + nummer_2)
        print("Was ist", nummer_1, "+", nummer_2, "?")

    elif zeichen == 2:
        right_answer = int(nummer_1 - nummer_2)
        print("Was ist", nummer_1, "-", nummer_2, "?")

    elif zeichen == 3:
        right_answer = int(nummer_1 * nummer_2)
        print("Was ist", nummer_1, "x", nummer_2, "?")
    elif zeichen == 4:
        right_answer = int(nummer_1 / nummer_2)
        print(f"Was ist {nummer_1} geteilt durch {nummer_2} ?")

    else:
        print("System Error\tkeine Aufgabe definiert")
        exit()
    answer = int(input("Antwort:\t\t"))

    if right_answer == answer:
        score = score + 1
        print("\nRichtig!!\n")
        print("Dein Score ist:\t", score)
        print("Als nächstes:\n_________________________________________\n_________________________________________")

    elif answer == 42:
        if Joker >= 1:
            Joker = Joker - 1
            score = score + 1
            print("\nRichtig!! 42 ist die Antwort auf alles.\n")
            print("Dein Score ist:\t\t\t", score)
            print(
                "Als nächstes:\n_________________________________________\n_________________________________________")
        else:
            print("42 darf nur einmal verwendet werden!")

    else:
        print("Du hast verloren!")
        print("Die richtige antwort war:\t", right_answer)
        print("Dein Score war: ", score, )
        game = 0

einleitung_1()
einleitung_2()
while game <= 1:
    if game == 1:
        while game == 1:
            game_loop()
    elif game == 0:
        print("\n____________________________________")
        print("Möchtest du noch weiter spielen?")
        weiter = input("[Y]es or [N]o\n\t")
        if weiter.lower() == "Y":
            game = 1
            score = 0

        else:
            exit()
input("Enter, um das Programm zu beenden")
