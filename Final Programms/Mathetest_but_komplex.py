import random
print("\t\t\t\t\tMathematik Test\n\n")
print("Bitte gebe eine beliebige Zahlen an.\nUm so hoeher, um so schwerer wird der Test.\n\t")
schwierigkeit = int(input("\t"))
print('Dieses Spiel zaehlt mit, wie viele Fragen du infolge richtig hattest.\nDas ist der sogenannte "Score".')
print('Dein "Score Goal" ist dein erwuenschter "Score". Dann wird das spiel pausiert\n')
score_goal = int(input('Welchen "Score" moechtest du heute erreichen? Wir empfehlen 50\n\t'))
print("\nGut, dann lass uns jetzt anfangen!")
print("\nBitte achte darauf, das du keine anderen Zeichen, außer deiner Antwortzahlen verwendest!")
print("___________________________________________________________________________________________________________")
game = 1
Joker = 1
score = 0

#               Variabeldefinierung
#
# score:            Gibt anzahl der richtigen antworten in folge an
# score_goal:       Gibt den Gewünschten Score des Anwenders an, wenn deiser erreicht wird, wird er
# schwierigkeit:    Gibt die maximale höhe der Zahlen an, die in der Aufgabenstellung möglich sind
# Joker:            Für den einmaligen gebrauch von der "42 Antwort" pro spiel
# nummer_1:         Die erste Zahl der Aufgabe
# nummer_2:         Die zweite Zahl der Aufgabe
# zeichen:          Für die zufällige Rechenzeichen definierung
# dive_else:        Wenn die geteilt aufgabe nicht möglich ist, wird stattdessen diesen zeichen verwendet
# game:             Wird nur für die "while-schleife" verwendet, um das spiel weiter laufen zu lassen oder abzubrechen
# answer:           Die antwort auf die aufgabe von dem Anwender
# right_answer:     Die richtige Antwort der Aufgabe

while game == 1:
    nummer_1 = random.randint(1, schwierigkeit)
    nummer_2 = random.randint(1, schwierigkeit)
    zeichen = random.randint(1, 4)
    devide_else = random.randint(1, 3)
    str(nummer_1)
    str(nummer_2)
    if zeichen == 4:
        if nummer_1 % nummer_2 == 0:
            zeichen = zeichen
        else:
            zeichen = devide_else

# Im folgenden Part (zeile 45 bis 56) wird eingeleitet, wenn das Score Goal errreicht wird.
# Hier wird nachgefragt, obman weiter spielen will.
# Wenn ja, dann wird solange gespielt, bis das neue Scor Goal erreit ist!

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

# Im folgenden Part (Zeile 61 bis 78) wird das random Rechenzeichen definiert und eingesetzt.
# Zusätzlich wird dann sofort die Frage an den Endnutzer gestellt und die richtige antwort definiert.

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
        print("Error Zeile 67")
        exit()

# In der folgenden Zeile (82) wird er Input des Anwenders angefragt, um die Aufgabe zu lösen

    answer = int(input("Antwort:\t\t"))

# Im folgenden Part (Zeile 84 bis 111) wird überprüft, ob die angegebene Antwort stimmt oder nicht
# Falls die Antwort nicht Stimmt, aber 42 ist, ist sie trozdem zulässig,
# doch dieser "Joker" darf nur einmal verwendet werden.
# Wer weiß, der weiß...

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
            print("Als nächstes:\n_________________________________________\n_________________________________________")
        else:
            print("42 darf nur einmal verwendet werden!")

    else:
        print("Du hast verloren!")
        print("Die richtige antwort war:\t", right_answer)
        print("Dein Score war: ", score,)
        game = 0

input("Enter, um das Programm zu beenden")
# ______________________________________________________________________________________________________________________
#                           Funktionen:
#        Score:
#            gibt die anzahl der richtig gelösten Matheaufgaben an
#        Aufgabe:
#            Verwendet random.randit um verschiedene Aufgabe zufällig zu generieren und die Rechenzeichen zu varieren
#            Wenn richtig gelöst, dann kommt die nächste Aufgaben
#            wenn falsch, wird das programm beendet
#
#        Asking Version:
#           die Schwierigkeit (beide random.randit uahlen in zeile 10-11) wird in dieser Programmversion
#           von dem Benutzer manuell Festgelegt festgelegt:
#           Ermöglicht einfache Schwierigkeitseinstellung des Programms
