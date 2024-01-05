import time as t

user_input = input("Enter your password and we try to break it:\n\t")
used_trys = 0
start_time = t.time()
char_list = []
for char in user_input:
    char_list.append(chr(0))


def entry(password):
    global used_trys, char_list
    entry_text = ""
    for char in char_list:
        entry_text += char

    if entry_text == password:
        print(f"\n\nPassword found: {entry_text}")
        print(f"Time:  {(t.time() - start_time):.4f} sec!")
        print(f"Try's: {used_trys}")
        exit(0)

    else:
        used_trys += 1


def loop(index):
    global char_list

    for y in range(0, 55296):
        char_list[index] = chr(y)
        # print(char_list[index])
        entry(user_input)


for position in range(0, user_input.count("") - 1):
    print(position)

    loop(position)
    if position > 0:
        position = -1

print("Not Found!")
