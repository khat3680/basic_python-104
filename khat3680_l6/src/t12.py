"""
------------------------------------------------------------------------
Program 12 lab 6
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-23"
------------------------------------------------------------------------
"""

from functions import gic 

value = float(input("Enter the GIC purchase value: $"))
years = int(input("Enter the number of years invested: "))
rate = float(input("Enter the GIC interest rate (%): "))
print()
final_value = gic(value, years, rate)

