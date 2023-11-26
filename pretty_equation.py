# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Bryce Wilkins
# Darroch Darroch
# Charlie Watkins
# Section: ENGR 102 536
# Assignment: Lab 4.13
# Date: 22/11/2023
#
#
import cmath

# Setup
A = int(input('Please enter the coefficient A: '))
B = int(input('Please enter the coefficient B: '))
C = int(input('Please enter the coefficient C: '))

# Logic
# or whatever the primary computing is
a = f'{"- " if A < 0 else ""}{"" if abs(A) == 1 else abs(A)}x^2'
b = f'{" - " if B < 0 else " + "}{"" if abs(B) == 1 else abs(B)}x'
if A == 0:
    b = f'{" - " if B < 0 else ""}{"" if abs(B) == 1 else abs(B)}'
c = f'{" - " if C < 0 else " + "}{abs(C)}'

# removing functions to avoid 'bugs'
if A == 0:
    a = ''
if B == 0:
    b = ''
if C == 0:
    c = ''

# is so purty
if A != 0:
    print(f'The quadratic equation is {a}{b}{c} = 0')
elif A == 0 and B > 0:
    print(f'The quadratic equation is {b}x{c} = 0')
else:
    print(f'The quadratic equation is {a}{b}{c} = 0')
