# Nicholas Shaw
# Python version 3.12.0
# Activity 5
# 11/03/2023

''' grade scale
95 - 100 = A+
90 - 94 = A
85 - 89 = B+
80 - 84 = B
75 - 79 = C+
70 - 74 = C
60 - 69 = D
below 60 = F'''

# Grading script with crade vales intergrated 
score = int(input("Enter grade score: "))
if score == 100 or score >=95 :
    result = print("Your grade is an A+")
elif score == 94 or score >=90 :
    result = print("Your grade is an A")
elif score ==89 or score >= 85 :
    result = print("Your grade is a B+")
elif score == 84 or score >= 80 :
    result = print("Your grade is a B")
elif score == 79 or score >= 75 :
    result = print("Your grade is a C+")
elif score == 74 or score >= 70 :
    result = print("Your grade is a C")
elif score == 69 or score >= 60 :
    result = print("Your grade is a D")
else : 
    result = print("Your grade is a F")

'To make this script i had used my activity 4 script as reference and formated the script to print grade results.'