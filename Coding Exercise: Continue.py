# Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5
#
# Zero is considered divisible by everything and should not be in the output
#
# The aim is to use the continue statement, but it's also possible to do this without continue

numbers = range(0, 21)

for number in numbers:
    if number % 3 != 0 and number % 5 != 0:
        print(number)
    else:
        continue
