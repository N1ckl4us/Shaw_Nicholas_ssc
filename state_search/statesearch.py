# Nicholas Shaw
#Python version 3.12.0
# 11/15/2023
# State Capitol Search Activity 10

# Allow for 5 Searches
# Save Results of search to state_result.txt

#########################################
# IMPORT THE STATES & CAPITOLS
#########################################

# 2. Explain why we start with an empty Dictionary
# A: Dictionaries in python has multiple keys ,and said keys can contain multiple values. By leaveing the dictionary blank when the script starts, a loop for searching can be made to import just those lines associated with the keys and values rather than reading the whole txt file.
# Create Blank Dictionary
states = {}

# 3. Explain how the FOR Loop here is used to import the data
#  and separate it into KEY / VALUE pairs.
# A: The for loop opens the txt file and begins reading the keys for a match on what the script user had input, if a match is found it stores the key values and begins read the values associated with it; then it re turns the key and its valyes to the python script.
# Import State & Capitol in the blank Dictionary
with open('states.txt', 'r') as f:

 for line in f:
    (key, val) = line.split(',')
    states[key] = val

# User must enter the name of the state to search
print ('STATE SEARCH SCRIPT')
print ('Please enter the name of 5 states to search for.')

# 4. Create a variable called count with an assigned value of 5
count = 5

##########################################
# LOOP THE SEARCH & WRITE TO EXTERNAL FILE
##########################################

# Open Report file
f= open('state_results.txt', 'w+')

# 5. Describe how the WHILE Loop uses the count variable as a control.
# A: The while loop uses the count variable which had a numerical value set to it as a part of the script which tells it to keep running until a certain condition is reached; in this case it uses the variable to keep track of how many successful searched it has completed, it starts with 5 searches and ends when there are 0 left.
# 6. How is the count variable updated?
# A: The count variable is updated by writeing the script to subtract from the total of the count variable by 1 after every successful search. This is dispalyed with the (count -= 1) portion of the script.
# 7. What is the effect?
# A: The count variable decrases by 1 after every successful search and stops when it has no searches left i.e count = 0
# 8. Explain how states[search] returns a value.
# A: The script stores the key input the script user had entered and reads the imported txt file until it matches a key with what the user had entered; once found it reads and imports the values associated with the key in the dictionary to the python script in a print statement.

# Use a Loop to run search 5 times
while count > 0:
    search = input('Enter Name of State: ').title()

    # Check the Dictionary for the State / Capitol result
    if search in states:
        print ('The Capitol of ' + search + ' is ' + states[search])
        count -= 1
        print ('Remaining number of searches: ', count)
        f.write('State: ' + search + ' Capitol: ' + states[search])
    else:
        print ("You have entered an incorrect value.")

###########################################

# 9. Rewrite the LOOP SEARCH Section above (Lines 22 - 28) to utilize with open()
# script has been changed was orriginally "f = open('states', 'r')
# 10. Test and confirm your script works before submitting to FSO!