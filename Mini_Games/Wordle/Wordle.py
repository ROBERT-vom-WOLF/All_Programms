import random
from symbols_n_words import german_words


def get_word():
    word = random.choices(german_words)
    word = str(word)
    letters = word.count("")
    word = word[2:letters - 3]
    word = word.lower()
    return word


while True:
    guess_list = []
    indicator_list = []
    user_input = "!System: variable_definition_default_string_for_capture!"
    input_list = []
    word = get_word()
    letters = word.count("")
    print(word)
    for char in word:
        guess_list.extend("_")
    print(guess_list)

    while True:
        durchgang = 0
        user_letters = user_input.count("")
        while user_letters != letters:
            user_input = str(input("Ihr Guess:\t"))
            user_letters = user_input.count("")
            print(user_letters)
            print(letters)
            print(word[durchgang:durchgang + 1])

        for cahr in user_input:
            input_list.extend("char")

        for char in input_list:
            stelle = word.find(char)
            if stelle == word[durchgang:durchgang+1]:
                indicator_list.extend("C")
            elif char in word:
                indicator_list.extend("I")
            else:
                indicator_list.extend("X")
            durchgang += 1
        print()
        print(indicator_list)
        print(guess_list)
        break