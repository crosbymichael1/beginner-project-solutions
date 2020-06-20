import random

user_points = 0
bot_points = 0

game = True

while game:
    randnum = random.randrange(0, 3)
    computer = random.choice(["rock", "paper", "scissors"])
    print("User Points: {} Computer Points: {}\n\n".format(user_points, bot_points))
    user = input("Rock, Paper, Scissors:\nMake a Move:").lower()

    if user == "rock" and computer == "scissors":
        print("user wins")
        print("Bot Chose: " + computer)
        user_points = user_points + 1
    elif user == "scissors" and computer == "paper":
        print("user wins")
        print("Bot Chose: " + computer)
        user_points = user_points + 1
    elif user == "paper" and computer == "rock":
        print("user wins")
        print("Bot Chose: " + computer)
        user_points = user_points + 1
    elif user == computer:
        print("Bot Chose: " + computer)
        print("Tie")
    else:
        print("Computer Wins")
        print("Bot Chose: " + computer)
        bot_points = bot_points + 1

    play_more = input("Would you like to play again? y/n\nEnter: ")

    if play_more == "n":
        game = False

