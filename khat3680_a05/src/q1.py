"""
------------------------------------------------------------------------
Program 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""from a1_functions import max_three

x = float(input("Please enter your first number:"))
y = float(input("Please enter your second number:"))
z = float(input("PLease enter your third number:"))
print()
ops = max_three(x, y, z)
print("The average of the two smaller values is:{}".format(ops))

