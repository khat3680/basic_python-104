"""
------------------------------------------------------------------------
Assignment 4 question 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

from q3_functions import num_day

number=int(input('Please enter a number between 1 and 7: '))
l=num_day(number)
print('The number {} corresponds to {}'.format(number,l))
