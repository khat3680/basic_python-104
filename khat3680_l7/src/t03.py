"""
------------------------------------------------------------------------
Program 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------
"""

from functions import population_growth

target=int(input('Target Population:'))
current=int(input('Current Population:'))
rate=int(input('Growth rate(%):'))

years=population_growth(target, current, rate)

print()

print('Years to reach target: {}'.format(years))