# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Bryce Wilkins
# Darroch Darroch
# Charlie Watkins
# Section: ENGR 102 536
# Assignment: Lab 6.12
# Date: 20/11/2023
#
#

import math

prism_side = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))


# setup for foil_needed
var1 = layers * 3 * prism_side ** 2
var2 = 3 * prism_side ** 2

# primary calculations
vis_area = (layers * prism_side) ** 2 * (math.sqrt(3) / 4)
foil_needed = (var1 + var2) / 2 * layers
total = vis_area + foil_needed

print(f'You need {total: .2f} m^2 of gold foil to cover the pyramid')
