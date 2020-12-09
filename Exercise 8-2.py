# Make a two player rock paper scissors game.
# Hint: Ask for player plays. Compare them. Print out a statement to congratulate the winner. Ask if they want to
#       start a new game.

import re

wins_1 = 0
wins_2 = 0
input1_works = False

player1 = str(input('Player 1, enter your move: '))
while input1_works == re.search('[Rr]ock|[Pp]aper|[Ss]cissor', player1):
    if input1_works:
        pass
    else:
        player1 = str(input('Player 1, please enter rock, paper, or scissor: '))

player1_clean = re.findall('[Rr]ock|[Pp]aper|[Ss]cissor', player1)
player1_final = player1_clean[0]

# while input1_works == False:
#     if player1 != 'rock' and player1 != '[Pp]aper' and player1 != '[Ss]cissor':
#         player1 = str(input('Player 1, please enter rock, paper, or scissor: '))
#     else:
#         input1_works = True

player2 = str(input('Player 2, enter your move: '))
input2_works = re.search('[Rr]ock|[Pp]aper|[Ss]cissor', player2)
player2_clean = re.findall('[Rr]ock|[Pp]aper|[Ss]cissor', player2)
player2_final = player2_clean[0]

if input2_works:
    pass
else:
    player2 = str(input('Player 2, please enter rock, paper, or scissor: '))

# while input2_works == False:
#     if player2 != '[Rr]ock' and player2 != '[Pp]aper' and player2 != re.search('[Ss]cissor+'):
#         player2 = str(input('Player 2, please enter rock, paper, or scissor: '))
#     else:
#         input2_works = True

if re.search('[Rr]ock', player1_final) and re.search('[Pp]aper', player2_final):
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

play_again = input('Would you like to play again? (Y/N)')

# Use regex to allow variations of rock, paper, and scissor(s)
# After game is complete, ask if they want to play again and if yes, restart game.
# Keep a tally of how many games each player has won. DONE