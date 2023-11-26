# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Bryce Wilkins
# Darroch Darroch
# Charlie Watkins
# Section: ENGR 102 536
# Assignment: Lab 4.15
# Date: 26/11/2023
#
#

###################### Part A ###########################
# create 3 variables for user to input t or f into

a = input('Enter True or False for a: ')
b = input('Enter True or False for b: ')
c = input('Enter True or False for c: ')

if a == "True" or a == 'T' or a == 't':
    a = True
else:
    a = False

if b == "True" or b == 'T' or b == 't':
    b = True
else:
    b = False

if c == "True" or c == 'T' or c == 't':
    c = True
else:
    c = False



####################### Part B ######################
# evaluate the three variables
# cant use if-else statements here
#

# and and
print(f'a and b and c: {a and b and c}')
# or or
print(f'a or b or c: {a or b or c}')


######################## Part C #######################
# no if-else here either
# only use: not, and, or.
#
# ugh
print(f'XOR: {a and not b or not a and c}')
# True = 2, false = 1.... write down the combinations in which adding those up would equal an even number
print(f'Odd number: {(a and b and c) or (a and not b and not c) or (not a and not b and c) or (not a and b and not c)}')