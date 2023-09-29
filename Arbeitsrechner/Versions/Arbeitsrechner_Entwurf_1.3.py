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
        print("Du hast bei sowohl bei deinem Arbeitsbeginn,\nals auch bei deinem Feierabend 0000 angegeben.")
    else:
        beginn_general = ED_Time - 800 - BD_Time
        beginn_int = int(beginn_general)
        beginn_str = str(beginn_general)
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
    ending_general = BG_Time + 800 + BD_Time
    ending_int = int(ending_general)
    if 1> BG_Time:
        print("Du hast bei sowohl bei deinem Arbeitsbeginn,\nals auch bei deinem Feierabend 0000 angegeben.")

    else:
        ending_general = BG_Time + 800 + BD_Time
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
            ending_str = ending_str(ending_str + "0")
            print("\n\nUm diese Uhrzeit musst du anfangen:")
            print(ending_str[1:2] + ":" + ending_str[3:5] + " Uhr")

elif 1 < ED_Time:
    if 1 < BG_Time:
        over_h = ED_Time - BG_Time
        int(over_h)
        if 1 > over_h:
            print("Deine vorraussichtlichen Überstunden:" + over_h)
        else:
            print("Du musst so viele Überstunden Zahlen:" + over_h)
    else:
        print("done")






else:
    print("esl etest test 2 jbdu hst a")








input("\t\t\t\t\tEnter, um das Programm zu beenden.")