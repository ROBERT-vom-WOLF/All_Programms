print("\t\t\t\t\tArbeitszeitenrechner:")
print("\t\t\tVorangaben: \n\t\t\t\tMindest Pause: 1h\n\t\t\t\tMindest Arbeitszeit: 7h")

Arbeits_stunden = 7
Pausen_stunden = 1
zeitumbruch_minute = 0
over_h_minute = 0
over_h_stunde = 0

beginn = input("Dein Arbeitsbeginn\t(bsp. 08:54):\n\t")
ending = input("Dein Feierabend\t(bsp. 17:32):\n\t")
bd_time = input("Deine zusätzliche Pause\t(bsp. 00:15):\n\t")
beginn_Stunde = beginn[0:2]
beginn_Minute = beginn[3:5]
ending_Stunde = ending[0:2]
ending_Minute = ending[3:5]
bd_Stunde = bd_time[0:2]
bd_Minute = bd_time[3:5]

#   print("Beginn eingabe:\t", beginn_Stunde, beginn_Minute)
#   print("Ende eingabe:\t", ending_Stunde, ending_Minute)
#   print("Pause eingabe:\t", bd_Stunde, bd_Minute)

beginn_stunde_int = int(beginn_Stunde)
beginn_minute_int = int(beginn_Minute)
ending_stunde_int = int(ending_Stunde)
ending_minute_int = int(ending_Minute)
bd_stunde_int = int(bd_Stunde)
bd_minute_int = int(bd_Minute)

#           Überprüfung des User-Inputs nach güligkeit der Eingabe, z.B. wenn eine Stundenangabe von 25 geamcht wird,
#                                                                        wird das Programm beendet

if beginn_stunde_int > 24:
    print("System:\tError Zeitberechnung, ungueltige Zeitangabe: Beginn, Stunde")
    exit()
if beginn_minute_int > 60:
    print("System:\tError Zeitberechnung, ungueltige Zeitangabe: Beginn, Minute")
    exit()
if ending_stunde_int > 24:
    print("System:\tError Zeitberechnung, ungueltige Zeitangabe: Endzeit, Stunde")
    exit()
if ending_minute_int > 60:
    print("System:\tError Zeitberechnung, ungueltige Zeitangabe: Endzeit, Minute")
    exit()
if bd_stunde_int > 24:
    print("System:\tError Zeitberechnung, ungueltige Zeitangabe: Pause, Stunde")
    exit()
if bd_minute_int > 60:
    print("System:\tError Zeitberechnung, ungueltige Zeitangabe: Pause, Minute")
    exit()

if beginn_stunde_int < 0:
    print("System:\tError Zeitberechnung, ungültige Zeitangabe: Endzeit Stundenangabe ungueltich")
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

if beginn_stunde_int == 0:
    if beginn_minute_int == 0:
        print("System:\tKeine Beginn Zeitangabe, Berechnet Beginn")
        if ending_stunde_int == 0:
            if ending_minute_int == 0:
                print("System:\tKeine generelle Zeitagaben, beende Programm")
                exit()
        beginn_stunde_int = ending_stunde_int - Arbeits_stunden - Pausen_stunden - bd_stunde_int
        beginn_minute_int = ending_minute_int - bd_minute_int
        # print("Berechnung:", beginn_stunde_int, beginn_minute_int)

elif ending_stunde_int == 0:
    if ending_minute_int == 0:
        print("System:\tKeine End Zeitangabe, Berechnet Ende")
        if beginn_stunde_int == 0:
            if beginn_minute_int == 0:
                print("System:\tKeine generelle Zeitagaben, beende Programm")
                exit()
        ending_stunde_int = beginn_stunde_int + Arbeits_stunden + Pausen_stunden + bd_stunde_int
        ending_minute_int = ending_minute_int + bd_minute_int
        # print("Berechnung:", ending_stunde_int, ending_minute_int)

elif ending_stunde_int > 0 and beginn_stunde_int > 0:
    print("System:\tZwei Zeitangaben, berechnet Überstunden")
    if beginn_stunde_int + Arbeits_stunden + Pausen_stunden + bd_stunde_int < ending_stunde_int or beginn_minute_int + bd_minute_int < ending_minute_int:
        print("Du machst ueberstunden plus")
        over_h_stunde = ending_stunde_int - beginn_stunde_int - Arbeits_stunden - Pausen_stunden - bd_stunde_int
        over_h_minute = ending_minute_int - beginn_minute_int - bd_minute_int

    elif beginn_stunde_int + Arbeits_stunden + Pausen_stunden + bd_stunde_int > ending_stunde_int or beginn_minute_int + bd_minute_int > ending_minute_int:
        print("Du machst ueberstunden minus")
        over_h_stunde = ending_stunde_int - beginn_stunde_int - Arbeits_stunden - Pausen_stunden - bd_stunde_int
        over_h_minute = ending_minute_int - beginn_minute_int - bd_minute_int

#           Rechenblöcke:

while beginn_minute_int < 0:
    print("System:\t Beginn, Minute below 0:", beginn_minute_int)
    beginn_stunde_int = beginn_stunde_int - 1
    zeitumbruch_minute = beginn_minute_int * (-1)
    beginn_minute_int = 60 - zeitumbruch_minute
    zeitumbruch_minute = 0
    print("System:\t Beginn, Minute:", beginn_minute_int)
    print("System:\tZeitumbruch Berechnet: Beginn, Minute")

while beginn_minute_int > 60:
    print("System:\t Beginn, Minute over 60:", beginn_minute_int)
    beginn_minute_int = beginn_minute_int - 60
    beginn_stunde_int = beginn_stunde_int + 1
    print("System:\t Beginn, Minute:", beginn_minute_int)
    print("System:\tZeitumbruch Berechnet: Beginn, Minute")

while ending_minute_int < 0:
    print("System:\t Ende, Minute below 0:", ending_minute_int)
    ending_stunde_int = ending_stunde_int - 1
    zeitumbruch_minute = ending_minute_int * (-1)
    ending_minute_int = 60 - zeitumbruch_minute
    zeitumbruch_minute = 0
    print("System:\t Ende, Minute:", ending_minute_int)
    print("System:\tZeitumbruch Berechnet: Ende, Minute")

while ending_minute_int > 60:
    print("System:\t Ende, Minute over 60:", ending_minute_int)
    ending_minute_int = ending_minute_int - 60
    ending_stunde_int = ending_stunde_int + 1
    print("System:\t Ende, Minute:", ending_minute_int)
    print("System:\tZeitumbruch Berechnet: Ende, Minute")

beginn_stunde_str = str(beginn_stunde_int)
beginn_minute_str = str(beginn_minute_int)
ending_stunde_str = str(ending_stunde_int)
ending_minute_str = str(ending_minute_int)

if beginn_stunde_int < 10:
    beginn_stunde_str = "0" + beginn_stunde_str
if beginn_minute_int < 10:
    beginn_minute_str = "0" + beginn_minute_str
if ending_stunde_int < 10:
    ending_stunde_str = "0" + ending_stunde_str
if ending_minute_int < 10:
    ending_minute_str = "0" + ending_minute_str

print("Beginn:\t", beginn_stunde_str, ":", beginn_minute_str, "Uhr")
print("Ende:\t", ending_stunde_str, ":", ending_minute_str, "Uhr")
print("Ueberstunden:\t", over_h_stunde, "Stunden und", over_h_minute, "minuten.")
