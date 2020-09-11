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

from functions import sum_partial_harmonic

n=int(input("Enter n:"))
sum_s=sum_partial_harmonic(n)
print("The sum of the series {} to {} is:{}".format(1,1/n,sum_s))