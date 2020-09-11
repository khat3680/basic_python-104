"""
------------------------------------------------------------------------
Program 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
'''
from a10_functions import add_matrices
 
num = ""
list1 = []
list2 = []
while len(num)!=12  or num.isdigit()==False:
    num = str(input("Enter 12 real numbers: "))
num = list(num)
 
 
count = 0
count2 = 6
for i in range(3):
    row = []
    row2 = []
    for x in range(2):
        row.append(int(num[count]))
        row2.append(int(num[count2]))
        count+=1
        count2+=1
    list1.append(row)
    list2.append(row2)
 
sum_1 = add_matrices(list1,list2)
print(sum_1)

'''
n=4
i=0
for i in range(n):
    print(i)
