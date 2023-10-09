numbers_list = ["0", "1", "2", "3", "4", "5", "6" "7", "8", "9"]

alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":",
               ",", ".", "<", ">", "/", "?", "|", "\\", "~", "`", "'", "\"", "§", "©", "®", "™", "€", "¥", "£", "¢",
               "¤", "µ", "°", "¬", "¦", "§", "±", "²", "³", "¼", "½", "¾"]
def check(question, user_input, list_kind="alp", Language="EN"):
    if list_kind == "alp":
        while user_input not in alphabet_list:
            user_input = input(question)
        return user_input
    elif list_kind == "num":
        while user_input not in numbers_list:
            user_input = input(question)
        return user_input
    elif list_kind == "sym":
        while user_input not in symbol_list:
            user_input = input(question)
        return user_input
