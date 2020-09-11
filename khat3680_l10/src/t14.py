"""
------------------------------------------------------------------------
Program 14
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
from functions import file_copy_n
fv_1=open('words.txt','r',encoding='utf-8')
fv_2=open('new_words.txt','w',encoding='utf-8')
number_1=int(input('Number of lines to copy:'))
d=file_copy_n(fv_1,fv_2,number_1)

