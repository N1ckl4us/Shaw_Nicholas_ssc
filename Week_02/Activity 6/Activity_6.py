# Nicholas Shaw
# 11/04/2023
# Python version 3.12.0
# Activity 6

# There Python Modules are imported into the script to provide access to time and random related functions
import random
import time
fight = True
# Prompt to allow user to choose the name for GOODGUY
goodguy = str(input("Enter your Knight's Name: "))
goodguy = "Sir " + goodguy

# 1. CHANGE THE LINE BELOW SO THE USER CAN ENTER A VALUE FOR BADGUY
badguy = str(input("Enter your Knight's Name: "))
badguy = "Sir " + badguy

# Once Upon A Time...
print(goodguy + ", a Knight in search of adventure, is wandering through the enchanted forest one day.")

# 2. WHAT ACTION DOES time.sleep(2) PERFORM?
# A: The action time.sleep(2) puts a 2 second delay before exucuting the next portion of the script and printint the result in the terminal.
time.sleep(2)

print("As " + goodguy + " reaches a clearing, he encounters the fearsome " + badguy + "!")

time.sleep(2)

print(goodguy + ": You, Sir, are a Blackguard and a coward! I challenge you to a duel!")
print(badguy + ": I'mma cut you, fool!")

# Good Guy Health
gghealth = 100
# Bad Guy Health
bghealth = 100

# Fight Sequence Loop
while True:
    # 3. EXPLAIN HOW GOODGUY / BADGUY HIT POINTS ARE GENERATED
    # A: The hit points are generated through a random number geration in the random.randint(1, 100) script and only works after importing the random function.
    # Good Guy / Bad Guy Hit Points
    gghit = random.randint(1, 100)
    bghit = random.randint(1, 100)
    # #######################################################

    # 4. WHAT PURPOSE DOES '\n' SERVE?
    # A: The purpose of "\n" is to be an escape sequence and is reffered as a new line character which continues the seuence onto a new line
    print("\n")

    # 5. FIND & CORRECT THE SYNTAX ERRORS. COMMENT OUT THE INCORRECT LINES AND
    # WRITE THE CORRECT CODE UNDERNEATH
    print(F"{goodguy} +  rolls a  + {gghit}")
    print(F"{badguy} +  rolls a  + {bghit}")
# incorect code for # 5 is print(goodguy + "rolls a" + gghit), and print(badguy + "rolls a" + bghit)

    # 6. EXPLAIN HOW THE VALUE IN DAMAGE IS CALCULATED
    # A: The damage is calculated by taking the random numbers generated from the gghit and bghit variables. Then said numbers are subtracted from character over health pool represented by gghealth and bghealth, the remaining number then triggers the conditional statement.
    # Damage Calculator
    if gghit > bghit:

        damage = gghit - bghit
        bghealth = bghealth - damage
        print(goodguy + " strikes " + badguy + " for a " + str(damage) + " hit!\n")

        if bghealth >= 100:
            print(badguy + ": Thou hast missed.\n")
        elif bghealth >= 75:
            print(badguy + ": Tis but a flesh wound.\n")
        elif bghealth >= 50:
            print(badguy + ": Alas! A fair strike! En garde!\n")
        elif bghealth >= 25:
            print(badguy + ": Thou art a worthy opponent.\n")
        elif bghealth < 10:
            print(badguy + ": I am beaten. Well fought...\n")
            break
    # #######################################################
    elif bghit > gghit:

        damage = bghit - gghit
        gghealth = gghealth - damage

        print(badguy + " strikes " + goodguy + " for a " + str(damage) + " hit!\n")

    # 7. CORRECT THE SYNTAX ERROR(S)
        if gghealth == 100:
            result = print(goodguy + ": Thou hast missed.\n")
        elif gghealth >= 75 or gghealth == 99 :
            result = print(goodguy + ": Tis but a flesh wound.\n")
        elif gghealth >= 50 or gghealth == 74:
            result = print(goodguy + ": Alas! A fair strike! En garde!\n")
        elif gghealth >= 25 or gghealth == 49:
            result = print(goodguy + ": Thou art a worthy opponent.\n")
        elif gghealth < 10:
            result = print(goodguy + ": I am beaten. Well fought...\n")
            break
    # #######################################################
    '''fixed the syntax error in the conditional statement (if gghelth =) to (if gghelth ==)
   and added a + in the fourth conditional statement in (print( goodguy ": Thou art a worthy opponent.\n")) 
    it now looks like (print( goodguy + ": Thou art a worthy opponent.\n") '''

# END OF LOOP ###############################################

# 8. PRINT A CONGRATULATORY STATEMENT HERE USING THE NAME OF THE WINNER (GOODGUY OR BADGUY)

print(F"This is the end of the valiant Knight Fight between {goodguy} and {badguy} which shall go down in the annals of history.\n")

# 9. PART 2
'In your own words, answer the following 4 questions on the use of the WHILE Loop in the script from Part 1: '

'HINT: The answer to #3 and #4 should not be the same.'
'1. Why are gghealth & bghealth initially set outside the WHILE Loop? '
# 1) Because we want the script to run as efficenty with as little code possible. So we wouldn't need health values to be place until the fight sequence starts.
'2. What events happen inside the WHILE Loop? '
# 2) The fight sequence which consist of announcing what damage each Knight rolls, then those values are subtracted from the health pool which triggers a conditional statement for the kinght with the most remaining health and breaks the loop.
'3. What Condition will end the WHILE Loop? '
# 3) The loop will break after the two kight roll their initial damage rolls, which triggers the conditional statement and breaks the loop using the break function in code.
'4. How is that Condition handled in the code?'
# 4) teh condition is handled through taking the damage vallue from the random roll, and subtracting it from the kights health pool which triggers the conditinal statements.