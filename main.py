from os import get_exec_path
import random
from secrets import choice
from unittest import result


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
        else:
            return "Paper covers rock. You lose"
    elif(player == "scissors"):
        if(computer=="rock"):
            return "Rock smashes scissors. You lose"
        else:
            return "Scissors cut paper. You win"
    else:
        if(computer=="rock"):
            return "Paper covers rock. You win"
        else:
            return "Scissors cut paper. You lose"
    
    

choices=get_choices()
result=check_win(choices["player"], choices["computer"])