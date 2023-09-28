abc = input("Ja oder Nein\t")
answer = "t"
loop = 1
def fragestellung():
    global abc
    if not abc.lower == "y" or not abc.lower == "n":
        abc = input("Ja oder Nein\t")
    return abc


while loop == 1:
    if abc.lower() == "y":
        answer = "Ja"
        loop = 0
    elif abc.lower() == "n":
        answer = "Nein"
        loop = 0
    else:
        fragestellung()
print(answer)

