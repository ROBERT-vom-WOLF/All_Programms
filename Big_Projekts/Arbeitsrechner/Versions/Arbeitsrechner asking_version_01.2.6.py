# Begriffdefinierung
# BG_Time (beginning_time) ist die Zeit des Arbeitsbeginns
# ED_Time (ending_time) ist die Zeit des Arbeitsendes
# BD_Time (breakduration_time) ist die dauer der Pause über der mindestpause

print("\t\t\t\t\tArbeitszeitenrechner:")
print("\t\t\tVorangaben: \n\t\t\t\tMindest Pause: 1h\n\t\t\t\tMindest Arbeitszeit: 7h")
print("\nBitte geben sie die Uhrzeiten in Militäricher schreibweise an! Bsp.: 8Uhr = 0800, 0,5 Stunden = 50\n\n\n")

Break_Time = int(input("\tWas ist deine vorgeschriebene Mindestpause?\t\t"))
BG_Time = int(input("\tWann ist dein  Arbeitsbeginn?\t\t"))
ED_Time = int(input("\tWann ist dein Feierabend?\t\t"))
BD_Time = int(input("\tWie viel zusätzliche Pause möchtest du?\t\t"))

# Der grund für die Else mit dem print("Error") Befehl liegt daran, dass es immer nur Zwei mögliche Ausgangsfälle
# geben soll. Wenn ich immer nur If else verwende, habe ich einen Festgelegten ausgangspunkt
# und einen "Anderen" der undefinierbar ist

if 1 > BG_Time:
    if 1 > ED_Time:
        # Wenn beide Variabeln auf Null gesetzt sind (also keine Angabe), wird das hier ausgeführt.
        print("Du hast bei sowohl bei deinem Arbeitsbeginn,\nals auch bei deinem Feierabend 0000 angegeben.")
    elif 0 < ED_Time:
        # Wenn diese Elif ausgeführt wird, ist der Feierabend angegeben, aber kein Arbeitsbeginn.
        beginn_general = ED_Time - 700 - BD_Time - Break_Time
        beginn_int = int(beginn_general)
        beginn_str = str(beginn_general)
        # Folgender IF ELSE block wird der Output verschönert und evt. eine Null vor Uhrzeiten vor 10:00Uhr eingefügt!
        # bsp: 9:00 Uhr => 09:00 Uhr
        # Ebenfalls wird der Output geprintet und das Programm vollendet.
        if beginn_int < 1000:
            beginn_final = "0" + beginn_str + "0"
            str(beginn_final)
            print("\n\nUm diese Uhrzeit musst du anfangen:")
            beginn_output = (beginn_final[1:2] + ":" + beginn_final[3:5] + " Uhr")
            print(beginn_output[0:9])
        elif beginn_int > 1000:
            print("\n\nUm diese Uhrzeit musst du anfangen:")
            print(beginn_int[1:2] + ":" + beginn_int[3:5] + " Uhr")
        else:
            print("Error Zeile: 40")
    else:
        print("Error Zeile: 42")


elif 1 > ED_Time:
    ending_general = BG_Time + 700 + BD_Time + Break_Time
    ending_int = int(ending_general)
    if 1 > BG_Time:
        # Wenn beide Variabeln auf Null gesetzt sind (also keine Angabe), wird das hier ausgeführt.
        print("Du hast bei sowohl bei deinem Arbeitsbeginn,\nals auch bei deinem Feierabend 0000 angegeben.")

    elif 0 < BG_Time:
        # Wenn diese Elif ausgeführt wird, ist der Feierabend angegeben, aber kein Arbeitsbeginn.
        ending_general = BG_Time + 700 + BD_Time + Break_Time
        ending_int = int(ending_general)
        ending_str = str(ending_general)
        # Folgender IF ELSE block wird der Output verschönert und evt. eine Null vor Uhrzeiten vor 10:00Uhr eingefügt!
        # bsp: 9:00 Uhr => 09:00 Uhr
        # Ebenfalls wird der Output geprintet und das Programm vollendet.
        if ending_int < 1000:
            ending_final = "0" + ending_str + "0"
            str(ending_final)
            print("\n\nUm diese Uhrzeit kannst du frühstens aufhören:")
            ending_output = (ending_final[1:2] + ":" + ending_final[3:5] + " Uhr")
            print(ending_output[0:9])
        elif ending_int > 1000:
            ending_str = str(ending_int)
            print("\n\nUm diese Uhrzeit kannst du frühstens aufhören:")
            print(ending_str[0:2] + ":" + ending_str[2:4] + " Uhr")
        else:
            print("Error Zeile: 71")
    else:
        print("Error Zeile: 73")

# Die beiden elif und if bestimmen, ob bei Feierabend und Arbeitsbeginn eine angabe gegeben sind.
# Wenn ja, dann werden die anzahl der Überstunden berechnet, die man bekommt oder zahlen muss.
elif 1 < ED_Time:
    if 1 < BG_Time:
        over_h = ED_Time - BG_Time - 700 - BD_Time - Break_Time
        int(over_h)
        str_over_h = str(over_h)
        # Folgender IF ELSE block wird der Output verschönert und evt. eine Null vor den  Uhrzeiten vor 10:00Uhr
        # eingefügt! bsp: 9:00 Uhr => 09:00 Uhr
        # Ebenfalls wird der Output geprintet und das Programm vollendet.
        if 1 < over_h:
            print("Deine vorraussichtlichen Überstunden:" + str_over_h)
        elif 0 > over_h:
            print("Du musst so viele Überstunden Zahlen:\t" + str_over_h[1:2])
        else:
            print("Error Zeile: 90")
    else:
        print("Error Zeile: 92")

else:
    print("Error Zeile: 95")

input("\t\t\t\t\tEnter, um das Programm zu beenden.")
