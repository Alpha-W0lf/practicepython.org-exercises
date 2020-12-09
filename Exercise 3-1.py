# Create a list. DONE
# Print out all elements of the list that are less than 5. DONE
# Extra: Instead of printing elements one by one, make a new list that has all the elements that are less than 5 and
#        print this list. DONE
# Extra: Write this in one line of code. ^^ TODO
# Extra: Ask user for a number and return a list that contains only elements from the original list that are smaller
#        than the given number. DONE

# z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
#
# print(z[1])
# if z[0] < 5:
#     print(z[0])

# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     if x < 5:
#         print(x)
#     else:
#         continue

# k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = []
#
# for x in k:
#     if x < 5:
#         y.append(x)
#     else:
#         continue
# print(y)

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
y = []
r = int(input('Please enter a number: '))

for x in z:
    if x < r:
        y.append(x)
    else:
        continue
print(y)
