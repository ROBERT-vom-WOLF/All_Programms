#Begriffdefinierung
#BG_Time (beginning_time) ist die Zeit des Arbeitsbeginns
#ED_Time (ending_time) ist die Zeit des Arbeitsendes
#BD_Time (breakduration_time) ist die dauer der Pause über der mindestpause

print("\t\t\t\t\tArbeitszeitenrechner:")
print("\t\t\tVorangaben: \n\t\t\t\tMindest Pause: 1h\n\t\t\t\tMindest Arbeitszeit: 7h")
print("\nBitte geben sie die Uhrzeiten in Militäricher schreibweise an! Bsp.: 8Uhr = 0800\n\n\n")


BG_Time = int(input("\tWann Arbeitsbeginn?\t\t"))
ED_Time = int(input("\tWann Feierabend?\t\t"))
BD_Time = int(input("\tWie viel zusätzliche Pause?\t\t"))

if 1 > BG_Time:
    if 1 > ED_Time:
        print("Du hast bei sowohl bei deinem Arbeitsbeginn als \n auch bei deinem Feierabend 0 angegeben.")
    else:
        Beginn = ED_Time - 800 - BD_Time
        beginn_int = int(Beginn)
        if beginn_int < 1000:
             beginn_final = "0" + Beginn + "0"
             str(beginn_final)
             print("\n\nUm diese Uhrzeit musst du anfangen:")
             beginn_output = (beginn_final[1:2] + ":" + beginn_final[3:5] + " Uhr")
             print(beginn_output[0:9])
        else:
            print("\n\nUm diese Uhrzeit musst du anfangen:")
            print(beginn_int[1:2] + ":" + beginn_int[3:5] + " Uhr")

else:
    print("hj")





















































































































input("\t\t\t\t\tEnter, um das Programm zu beenden.")