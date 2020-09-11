"""
------------------------------------------------------------------------
Lab 5 Question 13
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

from functions import loan

qualified = loan()

if(qualified == False):
    print("Qualified for a loan: False")
else:
    print("Qualified for a loan: True")

    
