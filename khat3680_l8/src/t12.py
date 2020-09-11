"""
------------------------------------------------------------------------
Program 12
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-06"
------------------------------------------------------------------------
"""
from functions import list_sums

a = []
b=[]
n = int(input("Enter number of values in both lists: "))

for i in range(0, n, 1):
    number = int(input("Enter a value for list 1 at {}:".format(i + 1)))
    a.append(number)
    number_1 = int(input("Enter a value for list 2 at {}:".format(i + 1)))
    b.append(number_1)

k=[]

k=list_sums(a,b)
print(k)