"""
------------------------------------------------------------------------
Program 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2020-01-13"
------------------------------------------------------------------------

from functions import matrix_stats

cols=int(input('Enter the number of columns'))
rows=int(input('Enter the number of rows'))
a=[]
for i in range(rows):
    a2=[]
    for j in range(cols):
        ele=int(input('Enter elements '))
        a2.append(ele)
a.append(a2)"""

from functions import matrix_stats
a2=[[5, 7],[-5, 5],[7, 11]]
print(matrix_stats(a2))

