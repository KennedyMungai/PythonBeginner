import random


def get_choices():
    player_choice=input("Enter a choice(rock, paper, scissors): ")
    computer_choice="paper"
    
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    
    return choices


choice=get_choices()
print(choice)


food=[
    "pizza",
    "carrots",
    "eggs"
]

dinner=random.choice(food)
print(dinner)