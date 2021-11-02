name = input("What is your name? ")
age = int(input("What is your age? "))

if 18 < age < 31:
    print("Hi {}! Welcome to the holiday party!".format(name))
else:
    print("Sorry {}, your not in the age group to go to the party.".format(name))