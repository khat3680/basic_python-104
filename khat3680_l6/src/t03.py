"""
------------------------------------------------------------------------
Question 3 Lab 5
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-23"
------------------------------------------------------------------------
"""

from functions import sum_all

start=int(input('Enter the start:'))
finish=int(input('Enter the end:'))
inc=int(input('Enter the increment: '))

sum_num=sum_all(start, finish, inc)

print("The sum of all numbers from {} to {} increment {} is: {}".format(start,finish,inc,sum_num))