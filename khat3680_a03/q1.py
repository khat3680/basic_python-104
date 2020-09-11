"""
------------------------------------------------------------------------
ASSIGNMENT 3 ; QUESTION 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-24"
------------------------------------------------------------------------
"""

no_of_balloons=int(input('Enter number of balloons:'))

no_of_children=int(input('Enter number of children:'))
print('')

balloons=(no_of_balloons)//(no_of_children)

print('Each child will receive {} balloons'.format(balloons))

balloons_left=int((no_of_balloons)-(balloons)*(no_of_children))

print('Balloons that won’t be distributed: {}'.format(balloons_left))






