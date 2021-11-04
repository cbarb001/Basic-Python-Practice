# modify the program to use a while loop to allow the player to keep guessing
# as an extra, allow the player to quite by entering 0 (zero) for their guess

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())


while guess != answer:
    if guess == 0:
        print("You have quite the game")
        break
    elif guess < answer:
        guess = int(input("Please guess higher"))
    else:   # guess must be greater than answer
        guess = int(input("Please guess lower"))

if guess == answer:
    print("Well done, you guessed it")