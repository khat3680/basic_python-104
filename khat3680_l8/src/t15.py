"""
------------------------------------------------------------------------
Program 15
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-06"
------------------------------------------------------------------------
"""
from functions import symmetric_difference
a=[]
b=[]
n = int(input("Enter number of values in list 1: "))
p = int(input("Enter number of values in list 2: "))

for i in range(0, n, 1):
    number = int(input("Enter a value for list 1 at {}:".format(i + 1)))
    a.append(number)
print('Values 1: {}'.format(a))
    
for j in range(0,p,1):    
    number_1 = int(input("Enter a value for list 2 at {}:".format(i + 1)))
    b.append(number_1)
print('Values 2: {}'.format(b))

k=[]
k=symmetric_difference(a,b)
print(k)