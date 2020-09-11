"""
------------------------------------------------------------------------
Functions for Programs 
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2020-01-11"
------------------------------------------------------------------------
"""


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    md=0
    for i in range(1,len(a)):    
        if  md <= a[i-1]-a[i] or md <= a[i]-a[i-1] :
            md = abs(a[i-1]-a[i])
    return abs(md)

def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid=False
    if name[0].isalpha() or name[0]=='_':
        for i in name:
            
            if i=='_' or i.isdigit() or i.isalpha():
                valid = True 
            else: 
                valid=False
    else:
        valid=False
    return valid
    
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    print(a)
    large=a[0]
    small=a[0]
    total=0
    average=0
    for i in range(len(a)):
        small=
        for j in range(len(a[i])):
            large=max(a[i])
            small=min(a[i])
            total+=a[i][j]
            average=total/(len(a[i]))
    return small, large, total, average/len(a)
 
            
    
    
            
            
        
        