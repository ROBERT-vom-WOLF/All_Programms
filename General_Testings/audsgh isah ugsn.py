import random
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("Start guessing...")
possible_words = ["Haus", "Auto", "Katze", "Hund", "Tisch", "Stuhl", "Buch", "Blume", "Garten", "Sonne", "Mond", "Sterne", "Schule", "Lehrer", "Schüler", "Kaffee", "Tee", "Wasser", "Feuer", "Erde", "Luft", "Musik", "Film", "Theater", "Stadt", "Land", "Telefon", "Computer", "Brot", "Butter", "Käse", "Obst", "Gemüse", "Sommer", "Herbst", "Winter", "Frühling", "Familie", "Freunde", "Liebe", "Glück", "Traurigkeit", "Angst", "Freiheit", "Reisen", "Abenteuer", "Lachen", "Weinen", "Sport", "Musik", "Kunst", "Farben", "Essen", "Trinken", "Schlafen", "Lesen", "Schreiben", "Spielen", "Lernen", "Entspannen", "Elefant", "Buchstabe", "Universum", "Geburtstag", "Wunderbar", "Schokolade", "Abenteuer", "Telefonat", "Apotheker", "Fantastisch"]
word = random.choice(possible_words)
guesses = ''
turns = 10
print(f"Gesucht:  {word}")
while turns > 0:
    failed = 0
    for char in word.lower():
        if char in guesses:
            print(char, end=""),
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print("You won")
        break
    guess = input("\tguess a character:\t")
    guesses += guess
    if guess.lower() not in word.lower():
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print(f"The right word was: {word}")
            print("You Lose")
