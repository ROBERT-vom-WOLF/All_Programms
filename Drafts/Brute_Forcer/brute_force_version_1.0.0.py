import time as t


def brute_force_single_letter(key):
    num = 0
    for _ in range(0, 55296):
        force_letter = chr(num)
        print(f"Brute Forcing...\t\t\t\t\t{num}:\t\t{force_letter}")
        if force_letter == key:
            print(f"----------------------------------------------------------\nMATCH FOUND!\tLETTER:\t\t{force_letter}\n----------------------------------------------------------")   # nopep8
            return force_letter
        num += 1
        if num == 55296:
            return "No match found\nKey secure\nResult: None"


def brute_force_main():
    key = input("Ihr Passwort:\t\t")
    force_start = t.time()
    letters = []
    for letter in key:
        char = brute_force_single_letter(letter)
        letters.append(char)
    finish_time = t.time()
    for _ in range(0, 20):
        print("\n")
    print("Process finished!\nKEY:\t\t\t\t\t", end="")
    for char in letters:
        print(char, end="")
    print(f"\nTime to Force: \t\t\t{finish_time - force_start} Seconds")
    if "No match found\nKey secure\nResult: None" in letters:
        return False
    else:
        return True


brute_force_main()
