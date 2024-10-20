# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for 
# and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. 
# If not, print an error message.

#first_name = input("Please enter your first name: ")
#last_name = input("Please enter your last name: ")

#def input(prompt):
#    while True:
#       name = input(prompt)
#        if len(input) >= 2:
 #           return input
 #       else:
  #          print("Input Error: Name must be at least 2 characters. Please enter name again.")
########


def get_name(prompt):
    while True:
        name = input(prompt)
        if len(name) >= 2:
            return name
        
        else:
            print("Input Error: Name must be at least 2 characters. Please enter name again.")

first_name = get_name("Please type your first name:")
last_name = get_name("Please type your last name:")
