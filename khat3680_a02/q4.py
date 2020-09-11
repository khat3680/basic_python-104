"""
------------------------------------------------------------------------
ASSIGNMENT 2  QUESTION 4
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-19"
------------------------------------------------------------------------
"""


date = int(input('Enter the date in MMDDYYYY :'))

year = date%10000

day = ((date%1000000)-year)//10000

month = date//1000000

print("{:0>2d}/{}/{}".format(day,month,year))
