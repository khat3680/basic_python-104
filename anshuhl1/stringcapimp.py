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
dot=None
str_new =None
my_str=None
if len(my_str)==0 :
    str_new=None
else:
    my_str = my_str[:1].upper() + my_str[1:]
    str_new=my_str
    for i in range(len(my_str)):
        if my_str[i]== "." :
            dot=1
            print(my_str[i+2].upper())
                ##print(my_str[:i+1])
            my_str[i+2].upper()
                
            str_new=my_str[:i+1] 
            str_new= str_new + my_str[i+2].upper()
            print(str_new)
                #break
    if dot!=1 :
        str_new=my_str
        
return str_new