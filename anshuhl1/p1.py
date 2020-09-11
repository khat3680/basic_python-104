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
'''
a=int(input('Enter the width floor 1:'))
b=int(input('Enter the length floor2:'))
floor_1=a*b
c=int(input('Enter the width floor 1:'))
d=int(input('Enter the length floor2:'))
floor_2=c*d
print(' no_of_tiles= ',(floor_1+floor_2))

no_of_packages=int(input('Enter the no. of packages :'))
tiles=6*(no_of_packages)

left=tiles-(floor_1+floor_2)


print('Number of tiles left :',left)
'''

def maxilist(list_num):
    total=0
    for var in list_num:
        total+=list_num[var]
    return total    

