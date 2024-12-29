import random

def dice_roll():
    while True:
        print("Press Enter to roll the dice and -1 to stop!")
        inp = input()
        if inp == "-1":
            print("Game Over!")
            break
        elif inp == "":
            num = random.randint(1,6)
            print(f"Number on Dice : {num}")
        else:
            print("Invalid input!")

dice_roll()