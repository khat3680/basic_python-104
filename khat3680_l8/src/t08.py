"""
------------------------------------------------------------------------
Program 8
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-06"
------------------------------------------------------------------------
"""

from functions import linear_search
a = []
n = int(input("Enter number of values in a list: "))

for i in range(0, n, 1):
    number = int(input("Enter a value at {}:".format(i + 1)))
    a.append(number)

v = int(input("Enter variable to search: "))

index = linear_search(a, v)

print("Index of {}: {}".format(v, index))
if index==-1:
    print('Element is not present')