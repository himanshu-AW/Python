import random

def check(user,comp):
    if user == comp:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if comp == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if comp == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if comp == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


while True:
    you = input("Enter a choice (rock, paper, scissors): ")
    STP = ["rock", "paper", "scissors"]
    if you in STP:
        computer = random.choice(STP)
        print(f"\nYou chose {you}, computer chose {computer}.\n")
        check(you,computer)

    else:
        print('You have Enter wrong option ')

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break