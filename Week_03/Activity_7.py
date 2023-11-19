# Nicholas Shaw
# 11/10/2023
# Python version 3.12.0
# Activiy 7
###################################################################################################
import time

# Custom Functions
# 2. DESCRIBE HOW THE INCLUDED countdown() FUNCTION WORKS
# A: The countdown function works by having input entry which the user can choose in the terminal and proceeds to sequentialy decrease the numerical value entered.
def countdown(n):
    while n >= 0:
        print (n)
        time.sleep(1)
        n -= 1

##################################################################################################
# Self Destruct Sequencer
# This is the custom function created to handle all of the Self Destruct
# features needed. There are a few steps involved in the process, so take a few
# moments to study how this function works and think about ways to make it better.
def self_destruct(x):

    # Set Destruct Codes
    authorized_test = "000-Destruct-0"
    authorized_final = "000-Destruct-1"

    # 3. CREATE VARIABLES (SIMILAR TO ABOVE) FOR THE COMMANDING OFFICER'S CODE (co_code)
    # EXECUTIVE OFFICER'S CODE (xo_code) & CHIEF ENGINEER'S CODE (ce_code)
    # Write your code here
    co_code = "117-ExecuteHalo-1"
    xo_code = "006-Noble-2"
    ce_code = "020-Arbiter-3"
##################################################################################################
    # Consider the following print statements. Could they be combined into a single print
    # statement and get the same result? (Answer: Yes) There are many ways to resolve
    # issues in scripting. You get to decide what works best for your script.
    #  Display Self Destruct Warning
    print ("--------------------- WARNING! ----------------------")
    print ("You have initiated the USR ARES Self Destruct Program")
    print ("_____________________________________________________")
    print ("You must provide Authorized Initiate Code to Proceed.")

##################################################################################################
    # Request Authorized Rank
    # 4. EXPLAIN THE SIGNIFICANCE OF THE int() FUNCTION IN THE FOLLOWING LINE:
    rank = int(input("Select Correct Rank:\n [1] Commanding Officer\n [2] Executive Officer\n [3] Chief Engineer\n RANK: "))
    # A. The int() or interpret function allows the python script to read and interpret the user input from the following input code, which then allows the script to follow the set conditional statements. 

##################################################################################################
    # Because we're expecting the user to enter a number above, the conditional statement
    # below is needed to convert those numbers into something more useful. Doing this helps
    # reduce the risk of the user introducing bad data into the script.
##################################################################################################
    # Retrieve Rank Initiate Code
##################################################################################################
    # Commanding Officer
    if rank == 1:
        code = co_code
        print ("Commanding Officer Confirmed.")
    # Executive Officer
    elif rank == 2:
        code = xo_code
        print ("Executive Officer Confirmed.")
    # Chief Engineer
    elif rank == 3:
        code = ce_code
        print ("Chief Engineer Confirmed.")
    else:
        print ("You are not authorized to initial Self Destruct.")


##################################################################################################
    # Enter Self Destruct Code: 000-Destruct-0 or 000-Destruct-1
##################################################################################################
    # Set Supplied Rank Code
    initiate = input("Enter Self Destruct Confirmation Code: ")

    # Compare Rank Codes
    if initiate == code:
        print ("Self Destruct Initiate Code: ACCEPTED")
        final_code = input("Enter Activation Code: ")
        if final_code == authorized_final:
            print ("Destruct Sequence Confirmed.")
            # 5. EXPLAIN THE SIGNIFICANCE OF X
            print (x, " seconds to Self Destruct.")
            # A. The variable x is the place holder that memorizes the numerical value the user had entered for the countdown sequence.
            print ("ALL HANDS ABANDON SHIP - THIS IS NOT A DRILL")
            countdown(x)
            print ("Have a nice day!")
            print ("BOOM!")
        elif final_code == authorized_test:
            print ("Destruct Sequence Test Order Confirmed.")
            print ("THIS IS A DRILL - THIS IS A DRILL")
            print ("Timer Set to: " + x + " seconds.")
        else:
            print ("Destruct Sequence Aborted.")


##################################################################################################
    # Program Ends
##################################################################################################
# Self Destruct
timer = int(input("Enter Countdown Length (in seconds): "))
self_destruct(timer)



# 6. LIST THE LOCAL VARIABLES AND GLOBAL VARIABLES USED THROUGHOUT THIS SCRIPT
# A.  Global variables in thsi script are "n, x, authorized_test, authorized_final"; local variables are "timer, rank, initiate, code, final_code".
# 7. LIST THE BUILT IN FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. Built in functions in the script are "countdown, time.sleep, print, and input".
# 8. LIST THE MODULE FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. The Module functions in this script are "def, time, and int".
# 9. LIST THE CUSTOM FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. Custom functions used in the script are "self_destruct".