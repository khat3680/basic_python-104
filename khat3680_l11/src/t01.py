"""
------------------------------------------------------------------------
Program 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-27"
------------------------------------------------------------------------
"""
from functions import generate_matrix_num

rows=int(input('The number of rows: '))
cols=int(input('The number of cols: '))
low=int(input('Low value: '))
high=int(input('High value: '))
value_type=input('Type of values:')

matrix_1=generate_matrix_num(rows,cols,low, high,value_type)

print(matrix_1)

