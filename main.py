import random

option = ["r", "p", "s"]


def start_game():
    print("------Welcome to the Rock-Paper-Scissors Game!------\nHere Are The Rules:\nRock beats Scissors\nPaper beats Rock\nScissors beat Paper!\nLet's Play!")
    pass


def getUser_choice():
    start_game()
    user_input = input("""\nKindly pick an option:\n"R" for "rock",\n"P" for "paper",\n"S" for "scissors."\nYour choice: """).lower()
    user_check = False
    while not user_check:
        if user_input == option[0]:
            user_choice = "Rock";
        elif user_input == option[1]:
            user_choice = "Paper";
        elif user_input == option[2]:
            user_choice = "Scissors";
        else:
            print("******ERROR******\nInvalid Option Entered.\nGame Restarted")
            getUser_choice()

        return user_choice
        break

def getComp_choice():
    rand_choice = random.choice(option)
    if rand_choice == option[0]:
        comp_choice = "Rock";
    elif rand_choice == option[1]:
        comp_choice = "Paper";
    elif rand_choice == option[2]:
        comp_choice = "Scissors";
    else:
        pass
    return comp_choice


def check_choices():
    user_choice = getUser_choice()
    comp_choice = getComp_choice()
    print(f"\nPlayer ({user_choice}): CPU ({comp_choice})")
    
    if user_choice == comp_choice:
        print(f"It's a tie!\nWe both selected {user_choice}.")
        check_choices()
    elif user_choice == "Rock":
        if comp_choice == "Scissors":
            print("Rock beats scissors!\nPlayer Wins!\nCPU Loses.\n****Game Ended****")
        else:
            print("Paper beats rock!\nCPU Wins!\nPlayer Loses.\n****Game Ended****")
    elif user_choice == "Paper":
        if comp_choice == "Rock":
            print("Paper beats rock\nPlayer Wins!\nCPU Loses.\n****Game Ended****")
        else:
            print("Scissors beats paper!\nCPU Wins!\nPlayer Loses.\n****Game Ended****")
    elif user_choice== "Scissors":
        if comp_choice == "Paper":
            print("Scissors beats paper!\nPlayer Wins!\nCPU Loses.\n****Game Ended****")
        else:
            print("Rock beats scissors!\nCPU Wins\nPlayer Loses.\n****Game Ended****")
    pass


check_choices()