import random
game = 1

kartenwert_1 = 0
kartenwert_2 = 0

karten = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

while game == 1:
    karte_1 = random.choices(karten, k=1)
    karte_2 = random.choices(karten, k=1)

    if karte_1 == "['J']" or "['Q']" or "['K']":
        kartenwert_1 = 10

    if karte_2 == "['J']" or "['Q']" or "['K']":
        kartenwert_2 = 10

    if karte_1 == "['A']":
        kartenwert_1 = 11

    if karte_2 == "['A']":
        kartenwert_2 = 11
# ___________________________________________________
    if 2 in karte_1:
        kartenwert_1 = 2
    if 3 in karte_1:
        kartenwert_1 = 3
    if 4 in karte_1:
        kartenwert_1 = 4
    if 5 in karte_1:
        kartenwert_1 = 5
    if 6 in karte_1:
        kartenwert_1 = 6
    if 7 in karte_1:
        kartenwert_1 = 7
    if 8 in karte_1:
        kartenwert_1 = 8
    if 9 in karte_1:
        kartenwert_1 = 9
    if 10 in karte_1:
        kartenwert_1 = 10

# ___________________________________________________

    if 2 in karte_2:
        kartenwert_2 = 2
    if 3 in karte_2:
        kartenwert_2 = 3
    if 4 in karte_2:
        kartenwert_2 = 4
    if 5 in karte_2:
        kartenwert_2 = 5
    if 6 in karte_2:
        kartenwert_2 = 6
    if 7 in karte_2:
        kartenwert_2 = 7
    if 8 in karte_2:
        kartenwert_2 = 8
    if 9 in karte_2:
        kartenwert_2 = 9
    if 10 in karte_2:
        kartenwert_2 = 10

# ___________________________________________________
    kartenwert_all = kartenwert_1 + kartenwert_2
# ___________________________________________________

    print("Deine Karten:\t", karte_1, karte_2)
    print("Dein gesamtwert:\t", kartenwert_all)


    input("~~~Enter~~~")
