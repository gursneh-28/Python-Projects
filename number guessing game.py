'''Task: Below are the steps:

1. Build a Number guessing game, in which the user selects a range.
2. Lets say User selected a range, i.e., from A to B, where A and B belong to Integer.
3. Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses'''

import random
import math

# taking range
a = int(input("Enter lower range : "))
b = int(input("Enter upper range : "))

# taking the random number
number = random.randint(a,b)

# number of guesses
count=round(math.log(b - a + 1, 2))
print("You've only ", count," chances to guess the integer!")


while count>0:
    guess = int(input("Guess the number: "))

    if guess==number:
        print("CONGRATULATIONS! You guessed correct")
        break
    elif guess<number:
        count -= 1
        print("Guessed Number is small")
        print("You have ", count, "chances left!")
    elif guess>number:
        count -= 1
        print("Guessed Number is large")
        print("You have ", count, "chances left!")


# print(count)
if count == 0:
    print("The number was", number)
    print("Better luck next time")