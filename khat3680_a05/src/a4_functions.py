"""
------------------------------------------------------------------------
Function for Program 4
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""

def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (int)
        y - y coordinate on a Cartesian plane (int)
    Returns:
        location - name of quadrant of coordinate x, y (str)
    -------------------------------------------------------
    """
    if(x == 0 and y == 0):
        location = "Q1"
    elif(x == 0 or y == 0):
        if(x == 0):
            location = "Q1"
        elif(y == 0):
            location = "Q2"
    elif(x < 0 and y > 0):
        location = "Q2"
    elif(x > 0 and y > 0):
        location = "Q1"
    elif(x < 0 and y < 0):
        location = "Q3"
    else:
        location = "Q4"
    
    return location
