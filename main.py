import random


def get_choices():
    player_choice=input("Enter a choice(rock, paper, scissors): ")
    computer_choice=random.choice(options)
    
    win_message="You win"
    lose_message="You lose"
    
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    
    options=[
        "rock", 
        "paper",
        "scissors"
    ]
    
    if(player_choice == computer_choice):
        return win_message
    else:
        return lose_message
    



food=[
    "pizza",
    "carrots",
    "eggs"
]

dinner=random.choice(food)
print(dinner)