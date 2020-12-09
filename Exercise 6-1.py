# Ask user for a string and print out whether the string is a palindrome or not (reads the same forward and backward)
# DONE

phrase = str(input('Please enter a palindrome. '))
list_phrase = list(phrase)
print(list_phrase)
x = 0
palindrome = False

while x < len(list_phrase):
    if list_phrase[x] == list_phrase[len(list_phrase) - (x + 1)]:
        x += 1
        palindrome = True
        continue
    else:
        palindrome = False
        break

if palindrome == True:
    print('This word IS a palindrome!!')
else:
    print('This word is NOT a palindrome. :(')

# DONE
