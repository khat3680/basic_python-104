"""
------------------------------------------------------------------------
Function for Program 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""

def pocket_color(num):
    """
    -------------------------------------------------------
    Returns the color of the number the ball landed on
    Use: color = pocket_color(num)
    -------------------------------------------------------
    Parameters:
        num - number that ball landed on (int > 0)
    Returns:
        color - color on which ball landed on
    -------------------------------------------------------
    """
    color = "none"
    if(num>36 and num<0 ):
        print('ERROR')
    if(num == 0):
        color = "green"
    elif(num >= 1 and num <= 10):
        if(num % 2 == 0):
            color = "black"
        else:
            color = "red"
    elif(num >= 11 and num <= 18):
        if(num % 2 == 0):
            color = "red"
        else:
            color = "black"
    elif(num >= 19 and num <= 28):
        if(num % 2 == 0):
            color = "black"
        else:
            color = "red"
    elif(num >= 29 and num <= 36):
        if(num % 2 == 0):
            color = "red"
        else:
            color = "black"
    else:
        color = "none"
    return color
    
