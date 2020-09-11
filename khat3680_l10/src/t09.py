"""
------------------------------------------------------------------------
Program D9
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
from functions import  count_frequency_value
fv = open('numbers.txt', 'r')

value = int(input("Value to count:"))
count = (count_frequency_value(fv, value))
print("{} appears {} time".format(value, count))
