"""
------------------------------------------------------------------------
Program Description
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

from functions import statistics

p = int(input("Enter number of values: "))

minimum, maximum, total, average = statistics(p)
print()
print("Minimum: {:.2f} \nMaximum: {:.2f} \nTotal: {:.2f} \nAverage: {:.2f}".format(minimum, maximum, total, average))

