# Nicholas Shaw
# Python version 3.12.0
# CTI2111-0
# Activity 3
# 10/29/2023

# numbers
A = 36
B = 137.62
C = 101.62
D = 17

# Variable math scripts are provided as comments above terminal results as print double-quote strings  
# Addtion example
"print(B+C)"
'''nick@Nicholass-MacBook-Pro Shaw_Nicholas_ssc % /usr/local/bin/python3 "/Users/nick/Desktop/Shaw_Nicholas_ssc/Week_01/Activity 3/Activity_3.py"
239.24'''
# Subtarction example
"print(A-D)"
'''nick@Nicholass-MacBook-Pro Shaw_Nicholas_ssc % /usr/local/bin/python3 "/Users/nick/Desktop/Shaw_Nicholas_ssc/Week_01/Activity 3/Activity_3.py"
19'''
# Multiplication example
"print(D*A)"
'''nick@Nicholass-MacBook-Pro Shaw_Nicholas_ssc % /usr/local/bin/python3 "/Users/nick/Desktop/Shaw_Nicholas_ssc/Week_01/Activity 3/Activity_3.py"
612'''
# Division example
"print(A/D)"
'''nick@Nicholass-MacBook-Pro Shaw_Nicholas_ssc % /usr/local/bin/python3 "/Users/nick/Desktop/Shaw_Nicholas_ssc/Week_01/Activity 3/Activity_3.py"
2.1176470588235294'''
# Exponentiation example
"print(B**C)"
'''nick@Nicholass-MacBook-Pro Shaw_Nicholas_ssc % /usr/local/bin/python3 "/Users/nick/Desktop/Shaw_Nicholas_ssc/Week_01/Activity 3/Activity_3.py"
2.1518870288626505e+217'''
# Modulus example 
"print(C%D)"
'''nick@Nicholass-MacBook-Pro Shaw_Nicholas_ssc % /usr/local/bin/python3 "/Users/nick/Desktop/Shaw_Nicholas_ssc/Week_01/Activity 3/Activity_3.py"
16.620000000000005'''

# Relational operators example
age = int(input('Enter Age:  '))
drivers_license = True

print(age)
if age > 65 :
    result= print("You are old enough to not be questioned on age when buying alcohol at a resturant.")
elif age < 2 :
    result= print("Please enter your real age.")
elif age >= 21 and drivers_license == True:
    result = print("You are old enough to drink alcohol at resurants but may need to present drivers license.")
elif age <= 5 :
    result = print("Please have your legal gaurdian proceed for you.")
elif age == 18 and drivers_license == True:
    result = print("You are considered a legal adult in the united states, but you must wait untill you are 21 to be the legal drinking age.")
elif age != 18: 
    result = print("You are not yet considered a legal adult in the United States.")







