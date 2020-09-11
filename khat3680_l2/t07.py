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

breakfast=float(input("Enter the cost of Breakfast :"))
lunch=float(input("Enter cost of lunch:"))
supper=float(input("Enter cost of supper:"))
total= breakfast+lunch+supper
print("")
print("{:<12s}".format("Meal"),"Cost")
print("{:<13s}${:>6.2f}".format("Breakfast",breakfast))
print("{:<13s}${:>6.2f}".format("Lunch",lunch))
print("{:<13s}${:>6.2f}".format("Supper",supper))
print("{:<13s}${:>6.2f}".format("Total",total))
