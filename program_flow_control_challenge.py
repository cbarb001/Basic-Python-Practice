# Write a program to print a number of options, and allow the user to select
# an option from the list.
# Make sure there are at least 4 options.
# The program should continue looping, allowing the user to choose one
# of the options each time around
# The loop should only terminate when the user chooses 0
# If the user makes a valid choice, the program should print a short message.
# The message should include the value that they typed
# Don't print a different message for each choice. Only change the number they typed.
# If their choice isn't one of the options in the menu,nothing should be
# printed. Although you will still see their input ont he screen
# Extra: modify the program so the menu prints again if they choose an invalid option.

answer = None
options = "Please select an option by entering the corresponding number to your answer: \n"\
          "What activity would you like to do today? \n"\
          "1. Go to the park \n"\
          "2. Play Soccer \n"\
          "3. Study Python \n"\
          "4. Dance \n"\
          "0. Exit out of program \n "

while answer != "0":
    answer = input(options)
    if answer in "1234":
        print("You chose to do option {}.".format(answer))
else:
    print("You have terminated the program")