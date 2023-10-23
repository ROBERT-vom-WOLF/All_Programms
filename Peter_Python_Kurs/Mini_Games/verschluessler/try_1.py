alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", "ü", "ö", "ä", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ü", "Ö", "Ä"]

numbers_list = ["0", "1", "2", "3", "4", "5", "6" "7", "8", "9"]

symbol_list = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":",
               ",", ".", "<", ">", "/", "?", "|", "\\", "~", "`", "'", "\"", "§", "©", "®", "™", "€", "¥", "£", "¢",
               "¤", "µ", "°", "¬", "¦", "§", "±", "²", "³", "¼", "½", "¾"]
text = "das wird jetzt verschlüsselt"
end_text = ""
schluessel = "B5342/"
devider = 0
multiplicator = 1
for char in schluessel:
    if char in alphabet_list:
        print(f"{char} is a Letter")
        devider += alphabet_list.index(char) + 1
    if char in numbers_list:
        print(f"{char} is a number")
        char = int(char)
        multiplicator += char
    if char in symbol_list:
        print(f"{char} is a Symbol")

multiplicator = multiplicator ** int(schluessel[1:2])
code_num = multiplicator // devider
print(code_num)

for char in text:
    number = code_num
    print(char)
    if char in alphabet_list:
        while number > len(alphabet_list) + 1:
            number -= len(alphabet_list) + 1
        char = alphabet_list[number:number + 1]
        print(char)
    end_text += str(char)
print(end_text)

