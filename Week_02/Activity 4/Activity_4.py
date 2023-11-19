# Nicholas Shaw
# Python version 3.12.0
# Activity 4
# 11/03/2023

# Activity variable inputs
age = int(input("Please enter your age: "))
citizen = int(input("Please enter how many years you have been a US citizen: "))

# Conditional statement
if age >=25 and age <30 :
    result = citizen
    if citizen == 7 or 8 :
        result = print("You are eligible to serve as a US Representative.")
elif age >= 29 :
    result = citizen
    if citizen >= 9 :
        result = print("You are eligible to serve as a US Representative or Senator.")
else:
    result = print("You are ineligible to serve as a US Representative or Senator position.")

    ''' During the creation of this script i could get the first and last conditional statement to wor but not the second
    after rewriting and troubleshooting the script for an hour and a half i realized that i had left the first conditional statement age 
    as >= 25 instead of its presented version, after many facepalms i made the correction to the statement and the script now functions as intented.'''