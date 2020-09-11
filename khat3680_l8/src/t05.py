"""
------------------------------------------------------------------------
Program 5
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-06"
------------------------------------------------------------------------
"""

from functions import get_lotto_numbers

n = int(input("Enter n: "))
low = int(input("Enter low: "))
high = int(input("Enter high: "))
values = get_lotto_numbers(n, low, high)
print("Lotto numbers: {}".format(values))

