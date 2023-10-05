# Tic Tac Toe
# Rock, Paper, Scissors
# Player vs computer random (r, p, s)



import random

def play():
    user = input('Welcome to Rock, Paper, Scissors. Please input R, P, S: ').upper()
    computer = random.choice(['R', 'P', 'S'])
    
    if computer == user:
        return('Its a tie! ')
    
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'
    
def is_win(player, opponent):
    
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    
print(play())
    
    
    