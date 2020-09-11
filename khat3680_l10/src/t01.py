"""
------------------------------------------------------------------------
Program 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-20"
------------------------------------------------------------------------
"""
from functions import customer_record 


fv=open('customer.txt','r',encoding='utf-8')
print('Find record n')
rec_num=int(input('Enter the record number to be printed: '))
list_=customer_record(fv,rec_num)

print(list_)

fv.close()

