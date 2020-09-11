"""
------------------------------------------------------------------------
Assignment 4 question 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-03"
------------------------------------------------------------------------
"""

from q1_functions import calc_federal_tax,calc_prov_tax

inc=float(input('Enter your income: $'))
print()
fed=float(calc_federal_tax(inc))
pro=float(calc_prov_tax(inc))

print('Your total tax liability is: ${:.0f} '.format(fed+pro))
print('[details federal tax: $ {:.0f}, state tax: $ {:.0f}]'.format(fed,pro))

