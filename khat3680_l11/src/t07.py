"""
------------------------------------------------------------------------
Program 7
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
from functions import find_position 
from t01 import matrix_1

rows=int(input('The number of rows: '))
cols=int(input('The number of cols: '))
low=int(input('Low value: '))
high=int(input('High value: '))


s_loc, l_loc = find_position(matrix_1)

print('Smallest Position : {}'.format(s_loc))
print('Smallest value: {}'.format(matrix_1[s_loc[0]][s_loc[1]]))

print('Largest Position : {}'.format(l_loc))
print('Largest value: {}'.format(matrix_1[l_loc[0]][l_loc[1]]))
