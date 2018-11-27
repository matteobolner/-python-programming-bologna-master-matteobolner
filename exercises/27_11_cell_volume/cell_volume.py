# diameter of a cell = 10 micrometers
# calculate the volume of the cell with python, given it is a perfect sphere
# use variables for parameters
# print the volume on  the screen


# this script calculates the volume of a spherical cell with a given diameter and prints it to the screen
from math import pi
diameter = 10
radius = (diameter/2)
volume = (4/3)*(pi)*((radius)**3)
print("The volume of an average cell (in micrometers) is: %s" %(volume))
