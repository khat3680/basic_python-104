"""
------------------------------------------------------------------------
Lab 4 Question 8
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from functions import computer_costs

cost=int(input('Enter cost of each computer: $'))
num=int(input('Enter number of computers: '))
comm=float(input('Enter Wholesaler Commision: %'))
print()
pre,post=computer_costs(cost, num, comm)
print('Cost of computers (no commission): ${:.2f}'.format(pre))
print('Cost of computers (total):         ${:.2f}'.format(post))

