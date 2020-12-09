# Take a given list and create a new list with only the even elements.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 0
# b = []
# while x < len(a):
#     if a[x] % 2 == 0:
#         b.append(a[x])
#         x += 1
#     else:
#         x += 1
#         continue
# print(b)

b = [x for x in a if x % 2 == 0] # <-- Looked up this answer (1 line of code)
print(b)