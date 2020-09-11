"""
------------------------------------------------------------------------
Lab 4 Question 7
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from functions import total_change


nic= int(input('Enter number of nickels: '))
dim= int(input('Enter number of dimes: '))
qua=int(input('Enter number of quarters: '))
lon=int(input('Enter number of loonies: '))
ton=int(input('Enter number of toonies:'))

tot=total_change(nic, dim, qua, lon, ton)
print()
print('Total amount : ${:.2f}'.format(tot))
