"""
------------------------------------------------------------------------
Lab 6 Program 10
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-23"
------------------------------------------------------------------------
"""

from functions import treadmill

burnt_per_minute=float(input('Enter calories burned per minute: '))
start=int(input('Enter beginning number of minutes:'))
end=int(input("Enter ending number of minutes: "))
inc=int(input('Enter the increment in minutes:'))

treadmill(burnt_per_minute, start, end, inc)

