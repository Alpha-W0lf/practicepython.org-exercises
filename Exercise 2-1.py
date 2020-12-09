# Ask the user for a number. DONE
# Tell the user if the number is odd or even. DONE
# Extra: If the number is a multiple of 4, tell the user. DONE
# Extra: Ask the user for two numbers. One number 'newnum' to check. One number 'divider' to divide by. If 'divider'
#        divides evenly into 'num', tell the user. If not, tell the user it does not.

num = int(input('Please enter a number: '))
num_check = num/2
num_remain = num%2
num_four = num%4
if num_remain == 0:
    print('This number is even.')
else:
    print('This number is odd.')
if num_four == 0:
    print('This number is divisible by four.')
else:
    print('This number is not divisible by four.')

newnum = int(input('Please enter another number: '))
divider = int(input('Please enter a divider: '))
newnum_check = newnum%divider
if newnum_check == 0:
    print('The first number is divisible by the second number.')
else:
    print('The first number is not divisible by the second number')