"""
-----------------------------------------------------------------------
Functions for lab 6
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-23"
------------------------------------------------------------------------
"""

def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    
    odd=0
    for i in range(1,num+1,2):
            odd+=i
        
    return odd

def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """ 
    
    for i in range(0,width+1,1):
        print (char*i)
    
    for i in range(width-1,0,-1):
        print (char*i)        
    
    return None

def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    print()
    for i in range(start,end+1,inc):
        cur_cal=burnt_per_minute*i
        print('Calories burned after {} minutes: {:.1f}'.format(i,cur_cal))
        
    return  

def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    rate = rate * 0.01
    print("Year       Value $")
    print("------------------")
    
    print("  0        ", end='')
    print("{:,.2f}".format(value))
    
    for year in range(1, years + 1, 1):
        value = value * rate + value 
        print("{:3.0f}".format(year), end='')
        print("{:16,.2f}".format(value))
        
    final_value = value
    return final_value


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    
    first_val = float(input("First value : "))
    maximum=first_val
    minimum=first_val
    
    total = 0
    for i in range(0,n):
        
        val = float(input("Next value {}: ".format(i + 1)))
    
        if(val <= minimum):
            minimum = val 
        if(val > maximum):
            maximum = val
        total += val
    avg = total / n
    return (minimum, maximum, total, avg)