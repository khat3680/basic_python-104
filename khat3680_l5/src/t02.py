"""
------------------------------------------------------------------------
Lab 5 Question 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-10"
------------------------------------------------------------------------
"""

from functions import get_weight

mass = float(input("Enter mass (kg): "))
weight, message = get_weight(mass)

print("Weight: {:.1f} N".format(weight))
print("Object is: {}".format(message))

