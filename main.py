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
    
    return choices



food=[
    "pizza",
    "carrots",
    "eggs"
]

dinner=random.choice(food)
print(dinner)