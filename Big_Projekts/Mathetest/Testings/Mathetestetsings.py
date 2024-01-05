import random
score = 0
print("\t\t\t\t\tMathematik Test\n\n")
schwierigkeit_1 = int(input("Bitte gebe jetzt eine Zahlen an.\nUm so höher, um so Schwerer.\n\t"))
print("\n\nGut, dann lass uns jetzt anfangen!")
print("\nAchte darauf, das du keine anderen Zeichen, außer deiner Antwortzahlen verwendest!")
while score < 999999999999999999999999999999999999999999999999999999999999999999:
    nummer_1 = random.randint(0, schwierigkeit_1)
    nummer_2 = random.randint(0, schwierigkeit_1)
    score = score + 1
    str(nummer_1)
    str(nummer_2)
    right_answer = int(nummer_1 * nummer_2)
    print("Was ist", nummer_1, "x", nummer_2, "?")
    answer = int(input("Antwort:\t\t"))
    if right_answer == answer:
        print("\nRichtig!!\n")
        print("Dein Score ist:\t\t\t", score)
        print("Als nächstes:\n________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    else:
        print("Falsch!! Du hast verloren!")
        print("Die richtige antwort war:\t", right_answer)
        score = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        input("Enter, um das Programm zu beenden")
# ______________________________________________________________________________________________________________________
#    Funktionen:
#        Score:
#            gibt die anzahl der richtig gelösten Matheaufgaben an
#        Aufgabe:
#            Verwendet random.randit um verschiedene Aufgabe zufällig zu generieren
#            Wenn richtig gelöst, dann kommt die nächste Aufgaben
#           wenn falsch, wird das programm beendet
#        Asking Version:
#           die Schwierigkeit (beide random.randit uahlen in zeile 10-11) wird in dieser Programmversion
#           von dem Benutzer manuell Festgelegt festgelegt:
#           Ermöglicht einfache Schwierigkeitseinstellung des Programms
