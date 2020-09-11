"""
------------------------------------------------------------------------
Function Module
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from math import sqrt

HOURS=24
DAYS=3600*(HOURS)
MINUTES=60


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: d = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        d - diameter of a circle (float)
    ------------------------------------------------------
    """
    dia=radius*2
    return dia

def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    
    NICKEL=0.05
    DIME=0.10
    QUARTER=0.25
    LOONIE=1.00
    TOONIE=2.00
    
    total= NICKEL*nickels + DIME*dimes + QUARTER*quarters + LOONIE*loonies + TOONIE*toonies
    return total

def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, a, v = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        a - area of the square pyramid (float)
        v - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sh=sqrt((base/2)**(2) + (height)**(2))
    area=base**(2) + 2*base*sqrt( (base/2)**(2) + (height)**(2) )
    vol= (base**(2)) * height/3
    
    return sh,area,vol

def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    pre=computer_cost*computers_bought
    post= pre+pre*(commission_percent)/100
    
    return pre,post

def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    
    
    
    days=int(initial_seconds//DAYS)
    hours=int((initial_seconds//3600)%HOURS)
    minutes=int((initial_seconds/MINUTES)%(MINUTES))
    sec=int(initial_seconds%(MINUTES))
    return days,hours,minutes,sec



    