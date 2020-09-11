"""
------------------------------------------------------------------------
Lab 4 Question 4
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from functions import square_pyramid

len=float(input('Enter length of base:'))

height=float (input('Enter the height'))

sh,a,v=square_pyramid(len, height)
print()
print('Slant height of square pyramid: {:.2f}'.format(sh))
print('Area of square pyramid: {:.2f}'.format(a))
print('Volume of square pyramid: {:.2f}'.format(v))