"""
------------------------------------------------------------------------
Function for Program 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""
from a2_functions import pocket_color

num = int(input("Enter a pocket number: "))

colors = pocket_color(num)
print()
if(colors == "none"):
    print("The pocket number entered is incorrect.")
else:
    print("The selected pocket is {}.".format(colors))
