print("\t\t\t\tSchlatjahrrechner:")
jahr = int(input("Welches Jahr?\t"))

jahr_4 = jahr / 4
jahr_100 = jahr / 100
jahr_400 = jahr / 400

if (jahr_4 % 2) == 0:
    if (jahr_100 % 2) == 0:
        print("Kein Schaltjahr")
    else:
        print("Das ist ein Schlatjahr")

elif (jahr_400 % 2 == 0):
    print("Das ist ein Schlatjahr")

else:
    print("Kein Schaltjahr")