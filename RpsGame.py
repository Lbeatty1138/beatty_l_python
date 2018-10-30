# import the random packages so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# arrays are a 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False


# win or lose function
def winorlose(status):
    print("call win or lose function")
    print("===========================================")
    print("you", status, " Would you like to play again")
    choice = input("Y / N: ")


# reset lives
    if choice == "Y" or choice == "y":

        # change globle variables
        global player_lives
        global computer_lives
        global player
        global Computer

        player_lives = 3
        computer_lives = 3
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice == "n ":
        print("you choose to quit")
        print("=================================")
        exit()


player_lives = 3
computer_lives = 3

# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0, 2)]

# print the choice to the terminal window
print("Computer chooses: ", computer_choice)

# set up our loop
while player is False:
    # set player to True by making a selection
    print("====================================")
    print("player lives:", player_lives, "/3")
    print("computer lives:", computer_lives, "/3")
    print("====================================")
    print("choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")
    print("player chooses:", player)


# check for a tie = choices are the same
    if (player == computer_choice):
        print("Draw!")
    # check to see if computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            player_lives = computer_lives - 1
            # the computer won
            print("You lose! Paper covers Rock!")
        else:
            # we have won
            print("You win!")

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player)
        else:
            print("You won!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You Lose", computer_choice, "smashes", player)
        else:
            print("You Win!", player, "cut", computer_choice)
    elif player == "quit":
        exit()
    else:
        print("Check your spelling... I don't get your human words\n")

# check for win or lose
    if player_lives is 0:
        winorlose("lose")

    if computer_lives is 0:
        winorlose("won")


# reset the game loop and start over again
    player = False
    computer = choices[randint(0, 2)]
