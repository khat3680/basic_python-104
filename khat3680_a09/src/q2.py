"""
------------------------------------------------------------------------
Program 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-23"
------------------------------------------------------------------------
"""
from a9_functions import find_median
fv_1=open('numbers.txt','r',encoding='utf-8')

fv_2=open('output_q2.txt','w',encoding='utf-8')

result=find_median(fv_1)
fv_2.write(result)

fv_1.close()
fv_2.close()
