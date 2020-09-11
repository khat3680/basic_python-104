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

no_1=float(input('Enter 1st number'))
no_2=float(input('Enter 2nd number'))
no_3=float(input('Enter 3rd number'))
no_4=float(input('Enter 4th number'))
no_5=float(input('Enter 5th number'))

b=input('Enter the number you want to print')
print()
if(b=='first'):
    print(no_1) 
elif(b=='second'):
    print(no_2)
elif(b=='third'):
    print(no_3)
elif(b=='fourth'):
    print(no_4)
elif(b=='fifth'):
    print(no_5)
if(b=='all'):
    print('{},{},{},{},{}'.format(no_1,no_2,no_3,no_4,no_4,no_5))
if(b=='none'):
    print('empty')

    