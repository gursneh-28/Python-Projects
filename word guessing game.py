'''In this game, there is a list of words present, out of which our interpreter will choose 1 random word.
The user first has to input their names and then, will be asked to guess any alphabet.
If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet.
The user will be given 12 turns(which can be changed accordingly) to guess the complete word.'''

import random

name = input("Enter your name: ")
print("Good Luck!", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

guessed_word = ['_'] * len(word)

print("Word = ", " ".join(guessed_word))
print("\nThe word to guess has", len(word), "letters.")

count = len(set(word)) +  5
print("You have", count ,"chances to guess!")

guessed=''

while count>0:
    guess = input("Guess the alphabet: ")

    if len(guess) != 1:
        print("Invalid Input !")

    elif guess in guessed:
        print("Already guessed!")

    elif guess in word:
        guessed+=guess
        for i in range(len(word)):
            if word[i]==guess:
                guessed_word[i] = guess

        if '_' not in guessed_word:
            print("Congratulations! You have guessed correctly the word : ", " ".join(guessed_word))
            break
        else:
            count-=1
            print("Word : ", " ".join(guessed_word))
            print("You have", count,"chances left!")


    else:
        print("Wrong")
        count-=1
        print("You have", count,"chances left!")

if count == 0:
    print("You are out of chances, the word was : ", word)
