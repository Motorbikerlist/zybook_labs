# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Bryce Wilkins
# Darroch Darroch
# Olivia Saint Loup
# Charlie Watkins
# Section: ENGR 102 536
# Assignment: Lab 3
# Date: 14/9/2023
#
#
# 93300758
#
def inout(var):
    return var

Value = float(input("Please enter the quantity to be converted: "))


toN = (float(Value * 4.44822))
a = (f'{Value:.2f} pounds force is equivalent to {toN:.2f} Newtons')
inout(a)
print(a)


m = (float(Value * 3.28084))
b = (f'{Value:.2f} meters is equivalent to {m:.2f} feet')
inout(b)
print(b)


atm = (float(Value * 101.325))
c = (f'{Value:.2f} atmospheres is equivalent to {atm:.2f} kilopascals')
inout(c)
print(c)

btu = (float(Value * 3.412141633))
d = (f'{Value:.2f} watts is equivalent to {btu:.2f} BTU per hour')
inout(d)
print(d)


Gpm = (float(Value * 15.850323074494))
e = (f'{Value:.2f} liters per second is equivalent to {Gpm:.2f} US gallons per minute')
inout(e)
print(e)


oF = (float(Value * (9 / 5) + 32))
f = (f'{Value:.2f} degrees Celsius is equivalent to {oF:.2f} degrees Fahrenheit')
inout(f)
print(f)
