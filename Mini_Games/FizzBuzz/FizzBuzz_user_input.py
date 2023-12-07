from symbols_n_words import numbers_list
user = "!System_original_str_define!"
while user[0] not in numbers_list:
    user = input("Deine Zahl\n\t")
user = int(user)
if user % 3 == 0 and user % 5 == 0:
    print("Fizz Buzz")
elif user % 3 == 0:
    print("Fizz")
elif user % 5 == 0:
    print("Buzz")
else:
    print(user)
