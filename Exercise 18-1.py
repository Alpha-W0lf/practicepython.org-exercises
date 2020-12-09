# cows and bulls game
# randomly generate a 4 digit number - DONE
# for every digit the user guesses correctly in the correct place, they have a cow TODO
# for every digit the user guesses correctly in the wrong place, they have a bull TODO
# every time the user guesses, tell them how many cows and bulls they have TODO
# once the user guesses the correct number, the game is over. TODO
# keep track of the user's total number of guesses and tell them at the end. TODO

import secrets

print('Welcome to the Cows and Bulls Game!')
print('We will randomly generate a 4 digit number and you will have to guess the number in as few tries as possible.')

secretnum = 1578 # secrets.randbelow(9999) TODO
guess = ''
guess_count = 0
cows = 0
bulls = 0

while True:
    guess = input("Input a 4 digit number as your guess: ")
    if len(str(guess)) == 4:
        try:
            guess = int(guess)
            print("That guess is a 4 digit number.")
            guess_count += 1
            print('You\'ve guessed', guess_count, 'time(s)')
            break
        except:
            print("That's 4 characters. Please enter a 4 digit number.")
            continue
    else:
        print("That's not 4 characters long.")

secretnum_list = [int(x) for x in str(secretnum)]
print(secretnum_list)
guess_list = [int(y) for y in str(guess)]
print(guess_list)

if secretnum_list[0] == guess_list[0]:
    cows += 1
    print('You have ', cows, ' cow(s) and ', (4 - cows), ' bull(s).', sep = '')
else:
    print('Nothing')


# compare list elements