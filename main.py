def get_choices():
    player_choice=input("Enter a choice: ")
    computer_choice="paper"
    
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    
    return choices


def greeting():
    return "Hi"


response=greeting()
print(response)


choice=get_choices()
print(choice)


