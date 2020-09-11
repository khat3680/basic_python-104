"""
------------------------------------------------------------------------
Program 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
'''
from a10_functions import word_freq
str_ = input("Enter a string: ")
dict_ = word_freq(str_)
length = len(dict_)
counter = 0
 
output = open("output_q3.txt","w")
 
if len(dict_)== 0:
    print(dict_)
    output.write("{}".format(dict_))
else:
    for k in dict_:
        if counter==length-1:
            print("{}: {}".format(k, dict_[k]))
            output.write("{}: {}".format(k, dict_[k]))
        else:
            print("{}: {}".format(k, dict_[k]))
            output.write("{}: {}\n".format(k, dict_[k]))
            counter+=1
'''

a=7
b=4
x=3.0
y=1.5
 

print('{0}'.fomat(b))
