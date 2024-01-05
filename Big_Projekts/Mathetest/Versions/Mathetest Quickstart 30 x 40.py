import random
score = 0
while score < 9999999999999999999999999999999999999999999:
    nummer_1 = random.randint(0, 20)
    nummer_2 = random.randint(0, 30)
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
#        Quickstart Version:
#           die Schwierigkeit (beide random.randit uahlen in zeile 10-11) wird in dieser Programmversion
#           ist im Quellcode vestgelegt und kann vom Endbenutzer nicht geändert werden:
#           Ermöglicht schnellers Spielen des Programms nach dem Start, ohne nervige fragen.
