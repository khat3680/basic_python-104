"""
------------------------------------------------------------------------
Program 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-14"
------------------------------------------------------------------------
"""
from a8_functions import string_capitalizer

string_1=input('Enter the text to edit \n')
str_fin=string_capitalizer(string_1)
if str_fin==None :
    print('No text entered')
else:    
    print('\n{}'.format(str_fin))
