# Which year do you want to check?


def leap_year(jahr):
    if jahr % 400 == 0:
        return "Leap Year"
    elif jahr % 100 == 0:
        return "Not a Leap Year"
    elif jahr % 4 == 0:
        return "Leap Year"
    else:
        "Not a Leap Year"


year = int(input("Year:\t\t"))
print(leap_year(year))
