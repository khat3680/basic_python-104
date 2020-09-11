"""
------------------------------------------------------------------------
Lab 4 Question 15
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
from functions import time_split

seconds=int(input('Enter the number of seconds: '))

days,hours,mins,sec=time_split(seconds)

print('Days: {}, Hours: {}, Minutes: {}, Seconds: {}'.format(days,hours,mins,sec))

