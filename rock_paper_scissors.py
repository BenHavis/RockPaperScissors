from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

playerWins = 0
compWins = 0

while compWins < 2 and playerWins < 2:

    player = input("Player, make your move: ").lower()
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            playerWins += 1
        else:
            print("computer wins!")
            compWins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            playerWins += 1
        else:
            print("computer wins!")
            compWins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            playerWins += 1
        else:
            print("computer wins!")
            compWins += 1
    else:
        print("Please enter a valid move!")

if playerWins == 2:
    print("You won!")
elif compWins == 2:
    print("The computer beat you")
