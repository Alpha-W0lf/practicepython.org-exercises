# Ask the user for a number. DONE
# Print a list of all the divisors of the number. DONE

num = int(input('Enter a number: '))
divisor = num
list = []

while divisor > 0:
    if num % divisor == 0:
        clean_num = divisor
        list.append(clean_num)
        divisor -= 1
    else:
        divisor -=1

list.sort()
print('Here is a list of all the divisors of your number: ', list)