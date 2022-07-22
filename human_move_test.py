

import random
global human_score
global computer_score
human_score = 0
computer_score=0

def human_move(human_score,computer_score) :
    while True:
        roll_request = input("Do you want to roll the dice: ")
        if roll_request == "y" or roll_request == "Y":
            roll = random.randint(1,6)
            if roll == 6:
                human_score =0
                print(f"The roll gave you {roll}") 
                print(f'Your current score is {human_score}')
                break
            else:
                human_score =  human_score + roll 
                print(f'roll gave you: {roll}')
                print(f'current score is: {human_score}')
        else:
            print(f"You have stopped playing this round, your current score is: {human_score} ")
            break

    return human_score,computer_score

def computer_move(human_score,computer_score):
    
    while computer_score !=30:
        roll = random.randint(1,6)

        if roll == 6:
            computer_score =0
            print(f"The roll gave you {roll}") 
            print(f'Your current score is {computer_score}')
            break
        else:
            computer_score =  computer_score + roll 
            print(f'roll gave you: {roll}')
            print(f'current score is: {computer_score}')

    return human_score,computer_score

human_move(human_score,computer_score)
computer_move(human_score,computer_score)
def is_game_over(computer_score, human_score):
    if computer_score or human_score ==50:
        print('Game is over: ')
#print(human_score)