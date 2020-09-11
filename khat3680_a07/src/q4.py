"""
------------------------------------------------------------------------
Program 4
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-09"
------------------------------------------------------------------------
"""

from a7_functions import find_value
from a7_functions import keep_positive_numbers

list_1 = keep_positive_numbers()

print("List entered: {}".format(list_1))

target = int(input("Enter target = "))

loc = find_value(list_1, target)

print("Target exists at location(s): {}".format(loc))