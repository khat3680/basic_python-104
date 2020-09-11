"""
------------------------------------------------------------------------
ASSIGNMENT 3 ; QUESTION 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-26"
------------------------------------------------------------------------
"""

number= int(input('Enter a positive two digit integer:'))

digit_one=number%10

digit_two=(number)//10

sum_digits=(digit_one) + (digit_two)
print('')
print('The sum of the two digits in the integer({})is: {}'.format(number,sum_digits) )

