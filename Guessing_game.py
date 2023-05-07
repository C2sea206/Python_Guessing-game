import random

random_number = random.randint(1,99)
guess = 0
while guess != random_number:
    guess = int(input("Guess a number between 1 and 99!"))

    if guess <  random_number:
        print ("Too Low!")
    elif guess > random_number:
        print ("Too high!")
    else:
        print ("YOU WIN!")