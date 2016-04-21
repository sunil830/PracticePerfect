"""
Author:     Sunil Krishnan
Date:       21-Apr-2016
Name:       RockPaperScissors.py
Reference:  http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
Problem Statement:
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)
Remember the rules:
Rock[1] beats scissors[2]
Scissors[2] beats paper[3]
Paper[3] beats rock[1]
"""


def gamelogic(p1,p2):
    if int(p1) == int(p2):
        v_result = 'Folks! its a tie'
    elif int(p1) - int(p2) in (-1,2):
        v_result = 'Player 1 wins!'
    elif int(p2) - int(p1) in (-1,2):
        v_result = 'Player 2 wins!'
    else:
        v_result = 'Unknown'
    print(str(v_result))


def playerinput():
    p1 = int(input('[Player 1 enter your choice: (Rock):1/(Scissors):2/(Paper):3] -: '))
    p2 = int(input('[Player 2 enter your choice: (Rock):1/(Scissors):2/(Paper):3] -: '))
    gamelogic( p1, p2 )

def controlgame():
    v_input = input('Please press Y to (start/restart) / N to (end) game: ').upper()
    v_game_num = 0
    while v_input != 'N':
        v_game_num += 1
        print('########################################')
        print('Starting game number: ' + str(v_game_num))
        playerinput()
        print('End Game Number: ' + str(v_game_num))
        print('########################################')
        v_input = input('Please press Y to restart / N to end game: ').upper()
        if v_input != 'Y':
            print('End Game Number: ' + str(v_game_num))
            print('########################################')
            break
    print('----------------------------------------')
    print('The number of games played is: ' + str(v_game_num))
    print('----------------------------------------')
if __name__ == '__main__':
    controlgame()
