import random

# convert int choice to strings
def choice_to_string(choice):
    if (choice > 3 or choice < 1):
        choice = int(input("Enter a valid input!! rock (1), paper (2), scissors(3):  "))
        return choice_to_string(choice)

    elif (choice == 1):
        return "rock"
    elif (choice == 2):
        return "paper"
    else:
        return "scissors"

# decide who wins between user and computer
def decide_winner(player, comp):
    if (player == comp):
        print("draw..")
        return "draw"
    elif ((player == 1 and comp == 2) or (player == 2 and comp == 1)):
        print("Paper beats rock..")
        return "paper"
    elif ((player == 1 and comp == 3) or (player == 3 and comp ==1)):
        print("Rock beats scissors..")
        return "rock"
    else:
        print("Scissors beats paper..")
        return "scissors"
    

# Main game loop
if __name__ == "__main__":
    while True:
        # player input
        print("Play rock, paper, scissors with the computer..")
        player_input = int(input("rock (1), paper (2), scissors(3)?"))
        player_choice = choice_to_string(player_input)

        # comp input
        comp_input = random.randint(1, 3)
        comp_choice = choice_to_string(comp_input)
        
        # print player and comp choices
        print(f"You chose {player_choice}")
        print(f"pc choice {comp_choice}")

        # decide winner of the game
        result = decide_winner(player_input, comp_input)
        if (result == player_choice):
            print("     YOU WIN!!")
        elif (player_choice == comp_choice):
            print("     IT'S A DRAW!!")
        else:
            print("     COMPUTER WINS!!")
        
        # play again
        ans = input("Play again? (Y/N):")
        if (ans == "n" or ans == "N"):
            print("thanks for playing")
            break

