import random

user = input("Pick rock, paper or scissors: ")

pc = random.choice(["rock", "paper", "scissors"])

print("User Chose {}".format(user))
print("Computer Chose {}".format(pc))


if user == "rock" and pc == "paper":
    print("Computer won")
elif user == "paper" and pc == "rock":
    print("user won")
elif user == "scissors" and pc == "paper":
    print("user won")
elif user == "paper" and pc == "scissors":
    print("Computer won")
elif user == "rock" and pc == "scissors":
    print("user won")
elif user == "scissors" and pc == "rock":
    print("Computer won")
else:
    print("tie game")


