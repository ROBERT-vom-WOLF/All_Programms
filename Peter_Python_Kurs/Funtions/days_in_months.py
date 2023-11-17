MONTHS_LIST = [["Januar", 31],
               ["Februar", 28],
               ["März", 31],
               ["April", 30],
               ["Mai", 31],
               ["Juni", 30],
               ["Juli", 30],
               ["August", 31],
               ["September", 30],
               ["Oktober", 31],
               ["November", 30],
               ["Dezember", 31]]

year = int(input("Welches Jahr?\n"))
month = int(input("Welcher Monat?\n"))
if year % 4 == 0 and not year % 100 == 0:
    print('["Februar", 29] (Schaltjahr)')
elif year % 400 == 0:
    print('["Februar", 29] (Schaltjahr)')
else:
    print(f"{MONTHS_LIST[month - 1]}")


main()
