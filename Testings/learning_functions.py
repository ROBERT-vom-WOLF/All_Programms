
def split(hour=0, second=0):
    if hour > 24 or second > 60:
        print("Zeitangaben ungueltig!")
        exit()
    else:
        str(hour)
        str(second)
        outprint = f"Es ist {hour}:{second} Uhr"
        return outprint


print(split(12, 34))

