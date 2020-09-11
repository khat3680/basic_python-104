"""
------------------------------------------------------------------------
Function for Program 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""


def max_three(x, y, z):
    """
    -------------------------------------------------------
    Calculates the average of the two smallest numbers
    Use: avg= max_three(x,y,z)
    -------------------------------------------------------
    Parameters: 
        x - value one (float>=0)
        y - value 2 (float>=0)
        z - value 3 (float>=0)
    Returns: 
        avg - average of the 2 smallest numbers
    -------------------------------------------------------
    """
    '''if(x<=y and y<=z):
    t=(x+y)/2
    elif(x<=y and z<=y):
    (x+z)/2
    elif(y+z):'''
        
    if(x >= y and x >= z):
        l = (z + y) / 2
    if(y >= x and y >= z):
        l = (x + z) / 2
    if(z >= x and z >= y): 
        l = (x + y) / 2
    
    return l  
    
