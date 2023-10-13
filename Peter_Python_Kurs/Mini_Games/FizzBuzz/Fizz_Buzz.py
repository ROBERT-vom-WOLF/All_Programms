for nummer in range(1, 101):
    if nummer % 15 == 0:
        print("Fizz Buzz")
    elif nummer % 3 == 0:
        print("Fizz")
    elif nummer % 5 == 0:
        print("Buzz")
    else:
        print(nummer)