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


def create_key():
    key = random.choices(alphabet_list, k=random.randint(0, 20))
    key += random.choices(numbers_list, k=random.randint(0, 20))
    key += random.choices(special_symbol_list, k=random.randint(0, 20))
    random.shuffle(key)
    key = str(key)
    key = key.replace("[", "")
    key = key.replace("]", "")
    key = key.replace("'", "")
    key = key.replace(",", "")
    key = key.replace(" ", "")
    return key


def read_key(key):
    devider = 0
    multiplicator = 1
    symbols_pos = 0
    for char in key:
        if char in alphabet_list:
            devider += alphabet_list.index(char) + 1
        if char in numbers_list:
            char = int(char)
            multiplicator += char
        if char in special_symbol_list:
            symbols_pos += special_symbol_list.index(char) + 1

    code_num = multiplicator * devider
    return int(code_num)


def create_crypt(text, key):
    symbol_pos = 0
    for char in str(key):
        if char in special_symbol_list:
            symbol_pos += special_symbol_list.index(char) + 1
    while symbol_pos > len(special_symbol_list):
        symbol_pos -= 1
    block_symbol = special_symbol_list[symbol_pos]
    crypt_text = ""
    durchgang_1 = 0
    possibilities = [True, False]
    for char in text:
        possible = random.choices(possibilities, weights=[20, 100])
        if possible:
            crypt_text += block_symbol
            add = random.choices(alphabet_list, k=(random.randint(1, 10)))
            add += random.choices(numbers_list, k=(random.randint(1, 10)))
            random.shuffle(add)
            for char in add:
                crypt_text += char
            crypt_text += block_symbol
        nummber = ord(char) + key + durchgang_1
        while nummber >= 110000:
            nummber -= 1
        crypt_text += chr(nummber)
        durchgang_1 += key // 2
    return crypt_text


def solve_crypt(text, key, schluessel):
    symbol_pos = 0
    for char in schluessel:
        if char in special_symbol_list:
            symbol_pos += special_symbol_list.index(char) + 1
    while symbol_pos >= len(special_symbol_list):
        symbol_pos -= 1
    block_symbol = special_symbol_list[symbol_pos]

    encrypt_text = ""
    durchgang_2 = 0
    for char in text:
        block_on_off = False
        if block_symbol in char and not block_on_off:
            block_on_off = True
        elif block_symbol in char and block_on_off:
            block_on_off = False
        elif not block_on_off:
            nummber_2 = ord(char) - key - durchgang_2
            while nummber_2 >= 110000 or nummber_2 < 0:
                nummber_2 += 1
            encrypt_text += chr(nummber_2)
            durchgang_2 += key // 2
    return encrypt_text


while True:
    user = input("Wollen sie [V]erschlüsseln oder [E]ntschlüsseln?\n\t").lower()
    if user == "v":
        text = input("Dein Text:\n")
        schluessel = create_key()
        key = read_key(schluessel)
        crypt_text = create_crypt(text, key)
        print(f"Der Key:\t\t{schluessel}\n")
        print(f"Der Text:\n\n{crypt_text}\n\n")

    elif user == "e":
        schluessel = input("Dein Key:\n\t")
        text = input("Dein Text:\n\t")
        key = read_key(schluessel)
        crypt_text = solve_crypt(text, key, schluessel)
        print(f"Der Key:\t\t{schluessel}\n")
        print(f"Der Text:\n\n{crypt_text}\n\n")

