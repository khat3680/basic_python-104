"""
------------------------------------------------------------------------
ASSIGNMENT 3 ; QUESTION 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-23"
------------------------------------------------------------------------
"""

mid_term=int(input('Enter your score in Midterm (0-100):'))
final_exam=int(input('Enter your score in Final (0-100):'))

exam= float(0.2*(mid_term) +  0.4*(final_exam))

print('')

print('Your weighted exam score is:{:.1f}'.format(exam))