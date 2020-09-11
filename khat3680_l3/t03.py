"""
------------------------------------------------------------------------
LAB 3  QUESTION 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""

LCHARGES=75
SCHARGES=50

lag=int(input('Number of large dogs groomed: '))

small=int(input('Number of small dogs groomed: '))

total=(lag)*(LCHARGES) + (SCHARGES)*(small)

print('Total earned for the day: ${:,.2f} '.format(total))

