import random
score = 0
print("\t\t\t\t\tMathematik Test\n\n")
print("Bitte gebe jetzt eine Zahlen an.\nUm so höher, um so Schwerer.\n\t")
schwierigkeit_1 = input("Schwierigkeit:\t")
print("\nGut, dann lass uns jetzt anfangen!")
print("\nAchte darauf, das du keine anderen Zeichen, außer deiner Antwortzahlen verwendest!")
int(schwierigkeit_1)
while score < 999999999999999999999999999999999999999999999999999999999999999999:
    nummer_1 = random.randint(1, schwierigkeit_1)
    nummer_2 = random.randint(1, schwierigkeit_1)
    zeichen = random.randint(1, 3)
    what_if_divided = int(nummer_1 / nummer_2)
    str(nummer_1)
    str(nummer_2)
    if zeichen == 1:
        right_answer = int(nummer_1 + nummer_2)
        print("Was ist", nummer_1, "+", nummer_2, "?")
    elif zeichen == 2:
        right_answer = int(nummer_1 - nummer_2)
        print("Was ist", nummer_1, "-", nummer_2, "?")
    elif zeichen == 3:
        right_answer = int(nummer_1 * nummer_2)
        print("Was ist", nummer_1, "x", nummer_2, "?")
    else:
        print("Error Zeile 33")
        right_answer = 999999999999999999999999999999999999999999999999999999999999999999999999999999999
    answer = int(input("Antwort:\t\t"))
    if right_answer == answer:
        score = score + 1
        print("\nRichtig!!\n")
        print("Dein Score ist:\t", score)
        print("Als nächstes:\n_________________________________________\n_________________________________________")
    elif answer == 42:
        score = score + 1
        print("\nRichtig!! 42 ist die Antwort auf alles.\n")
        print("Dein Score ist:\t\t\t", score)
        print("Als nächstes:\n_________________________________________\n_________________________________________")
    else:
        print("Falsch!! Du hast verloren!")
        print("Die richtige antwort war:\t", right_answer)
        print("Dein Score war: ", score,)
        score = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        input("Enter, um das Programm zu beenden")
# ______________________________________________________________________________________________________________________
#    Funktionen:
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
