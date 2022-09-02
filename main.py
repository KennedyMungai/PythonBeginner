import random


def get_choices():
    player_choice=input("Enter a choice(rock, paper, scissors): ")
    computer_choice=random.choice(options)
    
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    
    options=[
        "rock", 
        "paper",
        "scissors"
    ]
    
    return "Write the implementation logic"



def check_win(player, computer):
    print(f"You chose {player} ,the computer chose {computer}")
    
    if(player == computer):
        return "Its a tie"
    elif player == "rock":
        if(computer == "scissors"):
            return "Rock smashes scissors. You win!"
        elif(computer == "paper"):
            return "Paper covers rock. You lose"
    
    

check_win("rock", "paper")