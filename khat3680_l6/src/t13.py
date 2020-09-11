"""
------------------------------------------------------------------------
Program 13 lab 6
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-23"
------------------------------------------------------------------------
"""

from functions import lumber

b_min=int(input('Enter minimum value of base: '))
b_max=int(input('Enter maximum value of base: '))
b_inc=int(input('Enter increment in base value: '))
h_min=int(input('Enter minimum value of height: '))
h_max=int(input('Enter maximum value of height: '))
h_inc=int(input('Enter increment in height value: '))

lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)

