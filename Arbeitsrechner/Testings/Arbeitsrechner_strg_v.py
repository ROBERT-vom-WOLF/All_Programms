#                       Arbeitsrechner:
print("\t\t\t\t\tArbeitszeitenrechner:")
print("\t\t\tVorangaben: \n\t\t\t\tMindest Pause: 1h\n\t\t\t\tMindest Arbeitszeit: 7h")

Arbeits_stunden = 7
Pausen_stunden = 1
zeitumbruch_minute = 0

beginn = input("Dein Arbeitsbeginn\t(bsp. 08:54):\n\t")
ending = input("Dein Feierabend\t(bsp. 17:32):\n\t")
bd_time = input("Deine zusätzliche Pause\t(bsp. 00:15):\n\t")
beginn_Stunde = beginn[0:2]
beginn_Minute = beginn[3:5]
ending_Stunde = ending[0:2]
ending_Minute = ending[3:5]
bd_Stunde = bd_time[0:2]
bd_Minute = bd_time[3:5]

print(beginn_Stunde, beginn_Minute)
print(ending_Stunde, ending_Minute)
print(bd_Stunde, bd_Minute)

beginn_stunde_int = int(beginn_Stunde)
beginn_minute_int = int(beginn_Minute)
ending_stunde_int = int(ending_Stunde)
ending_minute_int = int(ending_Stunde)
bd_stunde_int = int(bd_Stunde)
bd_minute_int = int(bd_Stunde)

if beginn_minute_int > 60:
    beginn_stunde_int = beginn_stunde_int + 1
    beginn_minute_int = beginn_minute_int - 60

if ending_minute_int > 60:
    ending_stunde_int = ending_stunde_int + 1
    ending_minute_int = ending_minute_int - 60

while beginn_minute_int < 0:
    print("System:\t Beginn, Minute:", beginn_minute_int)
    beginn_stunde_int = beginn_stunde_int - 1
    zeitumbruch_minute = beginn_minute_int * (-1)
    beginn_minute_int = 60 - zeitumbruch_minute
    zeitumbruch_minute = 0
    print("System:\t Beginn, Minute:", beginn_minute_int)
    print("System:\tZeitumbruch Berechnet: Beginn, Minute")

while ending_minute_int < 0:
    print("System:\t Ende, Minute:", ending_minute_int)
    ending_stunde_int = ending_stunde_int - 1
    zeitumbruch_minute = ending_minute_int * (-1)
    ending_minute_int = 60 - zeitumbruch_minute
    zeitumbruch_minute = 0
    print("System:\t Ende, Minute:", ending_minute_int)
    print("System:\tZeitumbruch Berechnet: Ende, Minute")


if beginn_stunde_int > 24:
    print("System:\tFehler bei Zeitberechnung: Beginn, Stunde ungueltig ~~ Zeile: ")
    exit()

if ending_stunde_int > 24:
    print("System:\tFehler bei Zeitberechnung: Endzeit, Stunde ungueltig ~~ Zeile: ")
    exit()

if ending_stunde_int < 0:
    print("System:\tError Zeitberechnung, ungültige Zeitangabe: Endzeit Stundenangabe ungueltich")
    exit()
if beginn_minute_int < 0:
    print("System:\tError Zeitberechnung, ungültige Zeitangabe: Endzeit Stundenangabe ungueltich")
    exit()
if ending_minute_int < 0:
    print("System:\tError Zeitberechnung, ungültige Zeitangabe: Endzeit Stundenangabe ungueltich")
    exit()
