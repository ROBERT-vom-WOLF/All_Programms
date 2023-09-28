import random

difficulty = int(input("Bitte gebe jetzt eine Zahlen an.\nUm so höher, um so Schwerer.\n\t"))
nummer_1 = random.randint(1, difficulty)
nummer_2 = random.randint(1, difficulty)
nummer_3 = random.randint(1, difficulty)

mathezeichen_list_number = [1, 2, 3, 4]

#1 = + plus
#2 = - minus
#3 = * mal
#4 = / geteilt

zeichen1 = random.choice(mathezeichen_list_number)
zeichen2 = random.choice(mathezeichen_list_number)

int(zeichen1)
int(zeichen2)

print("Nummern:", nummer_1, nummer_2, nummer_3)
print("Zeichen", zeichen1, zeichen2)

aufgabe_str = "0"
aufgabe = 0

if zeichen1 == 1:
    if zeichen2 == 1:
        aufgabe = nummer_1 + nummer_2 + nummer_3
    elif zeichen2 == 2:
        aufgabe = nummer_1 + nummer_2 - nummer_3
    elif zeichen2 == 3:
        aufgabe = nummer_1 + nummer_2 * nummer_3
    elif zeichen2 == 4:
        aufgabe = nummer_1 + nummer_2 / nummer_3

elif zeichen1 == 2:
    if zeichen2 == 1:
        aufgabe = nummer_1 - nummer_2 + nummer_3
    elif zeichen2 == 2:
        aufgabe = nummer_1 - nummer_2 - nummer_3
    elif zeichen2 == 3:
        aufgabe = nummer_1 - nummer_2 * nummer_3
    elif zeichen2 == 4:
        aufgabe = nummer_1 - nummer_2 / nummer_3

elif zeichen1 == 3:
    if zeichen2 == 1:
        aufgabe = nummer_1 * nummer_2 + nummer_3
    elif zeichen2 == 2:
        aufgabe = nummer_1 * nummer_2 - nummer_3
    elif zeichen2 == 3:
        aufgabe = nummer_1 * nummer_2 * nummer_3
    elif zeichen2 == 4:
        aufgabe = nummer_1 * nummer_2 / nummer_3

elif zeichen1 == 4:
    if zeichen2 == 1:
        aufgabe = nummer_1 / nummer_2 + nummer_3
    elif zeichen2 == 2:
        aufgabe = nummer_1 / nummer_2 - nummer_3
    elif zeichen2 == 3:
        aufgabe = nummer_1 / nummer_2 * nummer_3
    elif zeichen2 == 4:
        aufgabe = nummer_1 / nummer_2 / nummer_3
else:
    print("ERROR!!")
nummer_1_str = str(nummer_1)
nummer_2_str = str(nummer_2)
nummer_3_str = str(nummer_3)

zeichen_1_str = str(zeichen1)
zeichen_2_str = str(zeichen2)

aufgabe_str_1 = (nummer_1_str, zeichen_1_str)
aufgabe_str_2 = (nummer_2_str, zeichen_2_str, nummer_3_str)

frage = (aufgabe_str_1, aufgabe_str_2)

print(frage)
print("Antwort:", aufgabe)
int(input("Was ist ihr Ergebniss?\n\t"))