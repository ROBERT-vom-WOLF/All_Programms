target = int(input("Input:\t"))
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}:\tFizzBuzz")
    elif number % 3 == 0:
        print(f"{number}:\tFizz")
    elif number % 5 == 0:
        print(f"{number}:\tBuzz")
    else:
        print(number)

