"""
------------------------------------------------------------------------
Program Description
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

from functions import *

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = float(input("Low value: "))
high = float(input("High: "))
value_type = input("Type of values: ")

matrix = generate_matrix_num(rows, cols, low, high, value_type)

print_matrix_num(matrix, value_type)
