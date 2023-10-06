user = input("Bitte trenne alle Ganzahlen mit einem Leerzeichen\nDeine Zahlen:\t\t")
liste = user.split(" ")
gesamtwert = 0
maximalwert = -99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for current_number in liste:
    current_number = int(current_number)
    if current_number > maximalwert:
        maximalwert = current_number
    gesamtwert += current_number
print(f"Gesamtwert:\t\t\t{gesamtwert}")
print(f"Durchschnitt:\t\t{gesamtwert / len(liste)}")
print(f"Die höchste Zahl ist:\t\t{maximalwert}")
