"""
------------------------------------------------------------------------
LAB 3  QUESTION 6
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
from cmath import exp
princi=int(input('Mortgage principal ($): '))

years=int(input('Number of years: ')*12)

rate=float(input('Yearly interest rate (%): '))/1200

monthlypay= float( (princi)*(rate*(1+rate)**(years))/((1+rate)**(years) -1)  )

print('The monthly payments are: $ {}'.format(monthlypay))


