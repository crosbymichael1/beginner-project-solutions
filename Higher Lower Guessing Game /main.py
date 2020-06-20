import random

game =  True
guesses = 0
newnumber = True

while newnumber:
    computer = random.randrange(1,101)
    while game:
        print("The computer randomly selects a number between 1 and 100 and you have to guess what the number is.\n")
        guesses = guesses + 1

        user = int(input("Guess the Number? "))

        if user > computer:
            print("You guessed {} but the number is lower".format(user))
        elif user < computer:
            print("You guessed {} but the number is higher".format(user))
        else:
            print("You guessed the number! Users Guess: {}    Actual Number: {}   Amount of Guesses: {}".format(user, computer, guesses))
            guesses = 0
            game = False

    play = input("Would you like to play again?: (y/n)")
    if play == "y":
        newnumber = True
        game = True
    else:
        newnumber = False