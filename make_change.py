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

from decimal import *

getcontext().prec = 2

pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = Decimal(pay) - Decimal(cost)
print(f'You received ${change:.2f} in change. That is...')

quarters = 0
dimes = 0
nickels = 0
pennies = 0
q = "quarters"
d = 'dimes'
n = 'nickels'
p = 'pennies'

# need to use Decimal() or else everything explodes
while change >= .25:
    quarters += 1
    change -= Decimal(.25)

while change >= .10:
    dimes += 1
    change -= Decimal(.10)

while change >= .045:
    nickels += 1
    change -= Decimal(.05)

while change > 0:
    pennies += 1
    change -= Decimal(.01)

if quarters == 1:
    q = 'quarter'
if dimes == 1:
    d = 'dime'
if nickels == 1:
    n = 'nickel'
if pennies == 1:
    p = 'penny'

if quarters > 0:
    print(f'{quarters} {q}')

if dimes > 0:
    print(f'{dimes} {d}')

if nickels > 0:
    print(f'{nickels} {n}')

if pennies > 0:
    print(f'{pennies} {p}')