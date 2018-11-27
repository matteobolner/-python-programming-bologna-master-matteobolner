# diameter of a cell = user input
# calculate the volume of the cell with python, given it is a perfect sphere
# use variables for parameters
# print the volume on  the screen


# this script calculates the volume of a spherical cell from the input diameter and prints it to the screen

from math import pi

#diameter = input("Write here the diameter of your cell:")
input_file = open("input_diameter.txt")
diameter = input_file.read()
radius = (float(diameter))/2
volume = (4/3)*(pi)*((radius)**3)
print("The volume of your cell (in micrometers) is: %f" %(volume))
