# Take two lists and write a program that returns a list that contains only the common elements between the lists (
#     without duplicates) DONE
# Make sure the list works on lists of varying sizes. DONE
# Extra: randomly generate two lists to test the program. DONE
# Extra: Write this in one line of code (hard to do).

import random

a = [1, 1, 2, 3, 5, 8, 13, 34, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 34, 34, 10, 89, 12, 13]

a = [1, 2, 3, 4, 5, 6, 6, 7, 7, 9, 2, 1, 22, 53, 565, 32, 5, 4, 56, 0, 90]
b = [1, 2, 3, 3, 3, 82, 6, 7, 7, 9, 1, 5, 3, 72, 88, 32, 5, 13, 12]

length1 = random.randint(15, 20)
length2 = random.randint(15, 20)

a = []
b = []
for i in range(0, length1):
    n = random.randint(0, 9)
    a.append(n)

for k in range(0, length2):
    m = random.randint(0, 9)
    b.append(m)

print(a)
print(b)

x = 0
c = []

while x < len(a) and x < len(b):
    if a[x] == b[x]:
        c.append(a[x])
        # print(a[x])
        x += 1
    else:
        x += 1

print(c)
c = list(dict.fromkeys(c))
print(c)

# DONE (except one line of code challenge)