import random
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

all_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", "ü", "ö", "ä", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ü", "Ö", "Ä", "0", "1",
                 "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2",
                 "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=",
                 "{", "}", ";", ":", ".", "<", ">", "/", "?", "|", "\\", "~", "`", "\"", "§"]

numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


special_symbol_list = ["©", "®", "™", "€", "¥", "£", "¢", "¤", "µ", "°", "¬", "¦", "§", "±", "²", "³", "¼", "½", "¾"]


def random_block_insert(schluessel):
    addition = ""
    possibilities = ["yes", "no"]
    possible = random.choices(possibilities, weights=[20, 100])
    if possible == ['yes']:
        number = schluessel.count("") - 2
        # symbol = special_symbol_list[number: number + 1]
        symbol = schluessel[number: number + 1]
        addition += str(symbol)    # hinzufügen von erstem zeichen des blocks
        add = random.choices(all_list, k=(random.randint(1, 20)))
        add_2 = random.choices(all_list, k=(random.randint(1, 20)))
        add += add_2
        for char in add:
            addition += char
        addition += str(symbol)    # hinzufügen von zweiten zeichen des blocks
        return addition
    return ""


def create_key():
    key = random.choices(alphabet_list, k=1)
    key += random.choices(numbers_list, k=4)
    key += random.choices(special_symbol_list, k=1)
    key = str(key)
    key = key.replace("[", "")
    key = key.replace("]", "")
    key = key.replace("'", "")
    key = key.replace(",", "")
    key = key.replace(" ", "")
    return key


def main_create(text, schluessel):
    end_text = ""
    devider = 0
    multiplicator = 1
    for char in schluessel:
        if char in alphabet_list:
            devider += alphabet_list.index(char) + 1
        if char in numbers_list:
            char = int(char)
            multiplicator += char

    multiplicator = multiplicator ** int(schluessel[1:2])
    code_num = multiplicator // devider
    code_num += 2000
    print(code_num)

    for char in text:
        # number = code_num
        number = 300
        while number > len(all_list) + 1:
            number -= len(all_list) + all_list.index(char)
        char = all_list[number:number + 1]
        char = str(char)
        char = char.replace("[", "")
        char = char.replace("]", "")
        char = char.replace("'", "")
        char = char.replace(",", "")
        end_text += char
        end_text += str(random_block_insert(schluessel))
    return end_text


def random_block_solve(unsolved, schluessel):
    solved = ""
    number = schluessel.count("") - 2
    symbol = schluessel[number: number + 1]
    block = False
    for char in unsolved:
        if char != symbol and not block:
            print(char)
            solved += char
        elif char == symbol:
            if block:
                block = False
            elif not block:
                block = True
    return solved


def main_solve(unsolved, key):
    print("solving...")
    solved = ""
    solved_rn = random_block_solve(unsolved, key)
    devider = 0
    multiplicator = 1
    for char in key:
        if char in alphabet_list:
            devider += alphabet_list.index(char) + 1
        if char in numbers_list:
            char = int(char)
            multiplicator += char

    multiplicator = multiplicator ** int(key[1:2])
    code_num = multiplicator // devider
    code_num += 2000
    print(code_num)
    for char in solved_rn:
        # number = code_num
        number = 300
        positions = len(all_list)
        char_position = all_list.index(char)
        while number > positions + 1:
            number -= positions + char_position + 1
        char = all_list[number - char_position:number - char_position + 1]
        char = str(char)
        solved += char

    return solved


v_or_e = ""
while True:
    v_or_e = input("[V]erschlüsseln oder [E]ntschlüsseln?\n\t").lower()
    if v_or_e == "v" or v_or_e == "e":
        break

text = input("Dein text:\n")

key = create_key()
created = main_create(text, key)
print(created)
print(f"\n\nKey: {key}")

solved = main_solve(created, key)
print(solved)
