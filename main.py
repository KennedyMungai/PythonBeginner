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
    if(player == computer):
        return "Its a tie"