# Begriffdefinierung
# BG_Time (beginning_time) ist die Zeit des Arbeitsbeginns
# ED_Time (ending_time) ist die Zeit des Arbeitsendes
# BD_Time (breakduration_time) ist die dauer der Pause über der mindestpause


print("\t\t\t\t\tArbeitszeitenrechner:")
print("\t\t\tVorangaben: \n\t\t\t\tMindest Arbeitszeit: 7h")
print("\nBitte geben sie die Uhrzeiten in Militäricher schreibweise an! Bsp.: 8Uhr = 0800, 0,5 Stunden = 50\n\n\n")

Break_Time = int(input("\tWas ist deine vorgeschriebene Mindestpause?\t\t"))
BG_Time = int(input("\tWann ist dein Arbeitsbeginn?\t\t"))
ED_Time = int(input("\tWann ist dein Feierabend?\t\t"))
BD_Time = int(input("\tWie viel zusätzliche Pause möchtest du?\t\t"))

# Der grund für die Else mit dem print("Error") Befehl liegt daran, dass es immer nur Zwei mögliche Ausgangsfälle
# geben soll. Wenn ich immer nur If else verwende, habe ich einen Festgelegten ausgangspunkt
# und einen "Anderen" der undefinierbar ist

if 1 > BG_Time:
    beginn_general = ED_Time - 700 - BD_Time - Break_Time
    beginn_int = int(beginn_general)
    beginn_str = str(beginn_general)
    if 1 > ED_Time:
        # Wenn beide Variabeln auf Null gesetzt sind (also keine Angabe), wird das hier ausgeführt.
        print("Du hast bei sowohl bei deinem Arbeitsbeginn,\nals auch bei deinem Feierabend 0000 angegeben.")
    elif :
        # Wenn diese Elif ausgeführt wird, ist der Feierabend angegeben, aber kein Arbeitsbeginn.
        if beginn_int < 1000:
            beginn_final = "0" + beginn_str + "0"
            str(beginn_final)
            print("\n\nUm diese Uhrzeit musst du anfangen:")
            beginn_output = (beginn_final[1:2] + ":" + beginn_final[3:5] + " Uhr")
            print(beginn_output[0:9])
        else:
            print("\n\nUm diese Uhrzeit musst du anfangen:")
            print(beginn_int[1:2] + ":" + beginn_int[3:5] + " Uhr")

elif 1 > ED_Time:
    ending_general = BG_Time + 700 + BD_Time + Break_Time
    ending_int = int(ending_general)
    if 1 > BG_Time:
        print("Du hast bei sowohl bei deinem Arbeitsbeginn,\nals auch bei deinem Feierabend 0000 angegeben.")

    else:
        ending_general = BG_Time + 700 + BD_Time + Break_Time
        ending_int = int(ending_general)
        ending_str = str(ending_general)
        if ending_int < 1000:
            ending_final = "0" + ending_str + "0"
            str(ending_final)
            print("\n\nUm diese Uhrzeit kannst du frühstens aufhören:")
            ending_output = (ending_final[1:2] + ":" + ending_final[3:5] + " Uhr")
            print(ending_output[0:9])
        else:
            ending_str = str(ending_int)
            print("\n\nUm diese Uhrzeit kannst du frühstens aufhören:")
            print(ending_str[0:2] + ":" + ending_str[2:4] + " Uhr")

elif 1 < ED_Time:
    if 1 < BG_Time:
        over_h = ED_Time - BG_Time - 700 - BD_Time - Break_Time
        int(over_h)
        str_over_h = str(over_h)
        if 1 < over_h:
            print("Deine vorraussichtlichen Überstunden:" + str_over_h)
        else:
            print("Du musst so viele Überstunden Zahlen:\t" + str_over_h[1:2])
    else:
        print("Logical Error")

else:
    print("Logical Error")

input("\t\t\t\t\tEnter, um das Programm zu beenden.")

