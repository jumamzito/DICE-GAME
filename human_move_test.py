import random
global human_score
global computer_score


def main():       
    human_score = 0
    computer_score=0

    instructions()

    while True:
        computer_score += computer_move(computer_score, human_score)
        human_score += human_move(computer_score, human_score)
        if is_game_over(computer_score, human_score):
            show_final_results(computer_score, human_score)
            break



def instructions():
    '''Tells the user the rules of the game.'''
    print ('"Dice is a simple game that involves two players taking turns; on each turn, a player rolls a six-\n'
          'sided die ("die" is the singular of "dice") as many times as they wish, or until they rolls a 6. Each \n'
          'number they rolls, except a 6, is added to their score this turn; but if they rolls a 6, their score for\n'
          'this turn is zero, and they turn ends. At the end of each turn, the score for that turn is added to the \n'
          'player\'s total score. The first player to reach or exceed 50 wins. \n'
          '  \n'
          'For example: \n' 
          '* Juma rolls 3, 5, 3, 1, and stops. His score is now 12. \n'
          '* Janet rolls 5, 4, 1, 1, 2, and stops. Her score is now 13. \n'
          '* Linda rolls 5, 3, 3, 5, 4, and stops. Her score is now 32 (12 + 20). \n' 
          '* Mumbi rolls 4, 6. She has to stop, and her score is still 13 (13 + 0). etc. \n'

          '  \n'
          'As defined above, the first player has an advantage. To make the game more \n'
          'fair, we will say that if the first player reaches or exceeds 50, the second \n'
          'player gets one additional turn. (If the second player is the first to reach \n'
          '50, the first player does not get an additional turn.)\n'
          '  \n'

          'If both players are tied with 50 or more, each gets another turn until the \n'
          'tie is broken. \n'
          '  \n'
          'Let\'s start! \n'
          '  \n'
          '****** \n'
          '  ')

def human_move(human_score,computer_score) :
    current_human_roll=0
    while True:
        roll_request = ask_yes_or_no()
        if roll_request:
            roll = roll()
            if roll == 6:
                print(f"The roll gave you {roll}") 
                print(f'Your current score is {human_score}')
                return 0
            else:
                human_score =  human_score + roll
                current_human_roll +=roll
                print(f'roll gave you: {roll}')
                print(f'current score is: {current_human_roll}')
            
        else:
            print(f"You have stopped playing this round, your current score is: {human_score} ")

            break

    return human_score,computer_score

def computer_move(human_score,computer_score):
    
    
    while computer_score !=30:
        roll = roll()

        if roll == 6:
            computer_score =0
            print(f"The roll gave you {roll}") 
            print(f'Your current score is {computer_score}')
            
            return 0
        else:
            computer_score =  computer_score + roll 
            print(f'roll gave you: {roll}')
            print(f'current score is: {computer_score}') 

    return human_score,computer_score

#human_move(human_score,computer_score)
#computer_move(human_score,computer_score)

def is_game_over(computer_score, human_score):
    if (computer_score >=50 or human_score >=50) and computer_score != human_score:

        return True
    
    else:
        return False



def ask_yes_or_no(prompt):
    prompt = input('Do You want to play the Game (Y/N):  ')
    if (prompt.startswith('Y') or prompt.startswith('y')) and prompt !="":
        
        return True
        
    elif (prompt.startswith('N') or prompt.startswith('n')) and prompt !="":
        return False

    else:
        ask_yes_or_no(prompt)

def roll():
    current_roll = random.randint(1,6)

    return current_roll

def show_current_status(computer_score, human_score):
    print(f'Your current score is : {human_score}')
    print(f'Computer score is : {computer_score}')

    if human_score > computer_score:
        print(f'You are ahead by : {human_score-computer_score}')

    else:
        print(f'You are behind by: {computer_score - human_score}')

def show_final_results(computer_score, human_score):
    if human_score > computer_score:
        print(f'Congratulations. You won the game by: {human_score - computer_score}')

    else:
        print(f'Better luck the next time. You lost the game by : {computer_score - human_score}')

#print(human_score)


if __name__ == '__main__':
        
    main()