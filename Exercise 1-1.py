# Create a program that asks the user to enter their name and age.
# Print out a message addressed to them and telling them the year they will turn 100 years old.
from datetime import date

name = input('Hello. Please enter your name:')
age = int(input('Now please enter your age: '))
added_years = ''

added_years = 100 - age
today = date.today()
current_year = today.year

print(name), print(age), print(added_years), print(current_year)
future_year = today.year + added_years
print(future_year)


print('Hello ', name, ', you will turn 100 in the year ', future_year, '.', sep = '')