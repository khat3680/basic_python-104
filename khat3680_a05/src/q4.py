"""
------------------------------------------------------------------------
Program 4
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""
from a4_functions import quadrant

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

location = quadrant(x, y)

print("The point ({}, {}) lies in {}".format(x, y, location))
