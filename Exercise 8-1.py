# Make a two player rock paper scissors game. DONE
# Hint: Ask for player plays. Compare them. Print out a statement to congratulate the winner. Ask if they want to
#       start a new game. DONE
wins_1 = 0
wins_2 = 0


def game():

    player1 = str(input('Player 1, enter your move: '))
    input1_works = False

    while not input1_works:
        if player1 != 'rock' and player1 != 'paper' and player1 != 'scissor':
            player1 = str(input('Player 1, please enter rock, paper, or scissor: '))
        else:
            input1_works = True

    player2 = str(input('Player 2, enter your move: '))
    input2_works = False

    while not input2_works:
        if player2 != 'rock' and player2 != 'paper' and player2 != 'scissor':
            player2 = str(input('Player 2, please enter rock, paper, or scissor: '))
        else:
            input2_works = True

    if player1 == 'rock' and player2 == 'paper':
        print('Player 2\'s paper beats rock!')
        wins_2 += 1
    elif player1 == 'paper' and player2 == 'scissor':
        print('Player 2\'s scissor beats paper!')
        wins_2 += 1
    elif player1 == 'scissor' and player2 == 'rock':
        print('Player 2\'s rock beats scissor!')
        wins_2 += 1
    elif player1 == 'rock' and player2 == 'scissor':
        print('Player 1\'s rock beats scissor!')
        wins_1 += 1
    elif player1 == 'paper' and player2 == 'rock':
        print('Player 1\'s paper beats rock!')
        wins_1 += 1
    elif player1 == 'scissor' and player2 == 'paper':
        print('Player 1\'s scissor beats paper!')
        wins_1 += 1
    else:
        print('Draw! You both have the same move.')

    print('Player 1 has', wins_1, 'wins.\nPlayer 2 has', wins_2, 'wins.')

    playagain = str(input('Would you like to play again? (y/n): '))
    input_playagain = False
    while not input_playagain:
        if playagain == 'y':
            print('Playing')
            input_playagain = True
            game()
        elif playagain == 'n':
            print('End of game.')
            print('The final score is:\nPlayer 1: ', wins_1, '\nPlayer 2: ', wins_2)
            break
        else:
            playagain = str(input('Would you like to play again? (y/n): '))


game()
# Use regex to allow variations of rock, paper, and scissor(s)
# After game is complete, ask if they want to play again and if yes, restart game. DONE
# Keep a tally of how many games each player has won. TODO tally keeps resetting to 0 - 0. need to fix.
