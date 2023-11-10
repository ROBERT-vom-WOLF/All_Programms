from random import randint

dice_numbers = [1, 2, 3, 4, 5, 6]

for _ in range(1, 20):
    dice_num = randint(0, 5)
    print(dice_numbers[dice_num])
