"""
------------------------------------------------------------------------
Lab 5 Question 5 
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-10"
------------------------------------------------------------------------
"""

from functions import is_leap

year = int(input("Enter a year (>0): "))


n = is_leap(year)

if(n == False):
    print("{} is not a leap year".format(year))
else:
    print("{} is a leap year".format(year))
    
    