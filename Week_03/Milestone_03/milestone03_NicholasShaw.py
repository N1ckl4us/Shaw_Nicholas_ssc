# Nicholas Shaw
# 11/13/2023
# Python version 3.12.0
# Pirate Swashbuckle Fight Milestone 3

import random
# 1. Import the utilities file
import utilities
from utilities import importer, randomator

# 2. Import the pirates.txt file
characters = importer('pirates.txt')

# dodge > parry > thrust > dodge
attack =['dodge', 'parry', 'thrust']

# 3. Use the utilites to randomly pick pirates for player and opponent
with open('pirates.txt', 'r') as file:
    characters = file.read().splitlines()
    player = randomator(characters)
    opponent = randomator(characters)

# 4. Add a while loop so that the pirates are not the same
while player == opponent :
    opponent = randomator(characters)

print ("Advast ye swabs, a fight betwixt \n" + player + " & " + opponent + " 'tis bout to commence! ")

pscore = 0
oscore = 0
gameover = False

while gameover == False:
    # This has changed for milestone 3. The game will still end when the player or opponent reaches 3. 
    if pscore >= 3:
        print (player + " has vanquished " + opponent)
        print ("Hip hip huzzah!")
        gameover = True
        break
    elif oscore >= 3:
        print (opponent + " has vaquished " + player)
        print ("Oh Captain, my Captain!")
        gameover = True
        break
    # 5. Exception - Add a while True and exception. 
    # Example: the player attack variable should allow the user to pick between the different types     
    while True: 
     try:
      pattack = int(input("please enter [1] dodge, [2] parry, [3] thrust: "))
      break
     except ValueError:
        print('Please enetr previous given values')

    # 6. Player only - Create an if/elif statement to set the number entry to the correct attack.
    if pattack == 1:
        pattack = 'dodge'
    elif pattack == 2:
        pattack = 'parry'
    elif pattack == 3:
        pattack = 'thrust'
    elif pattack >= 4:
        print("your indecisiveness has led to the crowd making a decision for you.")
        pattack = utilities.randomator(attack)

    # The program randomly picks the attack for the opponent
    oattack = utilities.randomator(attack)

    # 7. Add a while loop so that the attacks are not the same. Use the utilities module.
    while pattack == oattack:
        oattack = utilities.randomator(attack)

    print (player + " attacks with a " + pattack)
    print (opponent + " attacks with a " + oattack)

    # 8. Change your if/elif statment from milestone 2. Use the and to compare the attacks. All attacks must be used correctly.
    if pattack == oattack :
        result =  print("Both pirates execute the same manevour, and the moves cancel each other out.")
    elif pattack == 'dodge' and oattack == 'parry' :
        pscore += 1
    elif oattack == 'dodge' and pattack == 'parry' :
        oscore += 1
    elif pattack == 'parry' and oattack == 'thrust' :
        pscore += 1
    elif oattack == 'parry' and pattack == 'thrust' :
        oscore += 1
    elif pattack == 'thrust' and oattack == 'dodge' : 
        pscore += 1
    elif oattack == 'thrust' and pattack == 'dodge' : 
        oscore += 1
      

    # 9. Print a string that includes the player and the players score.
    print( "Score: " + player + str(pscore))
    # 10. Print a string that includes the opponent and the opponents score.
    print( "Score: " + opponent + str(oscore))

