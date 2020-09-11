"""
------------------------------------------------------------------------
Program 03
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-20"
------------------------------------------------------------------------
"""
from functions import customer_best
fv=open('customer.txt','r',encoding='utf-8')

print('Find customer with largest balance: ')

list_1=customer_best(fv)
print('{}'.format(list_1))

fv.close()     
    