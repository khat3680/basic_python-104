"""
------------------------------------------------------------------------
Functions for Program 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""

def base_price(length):
    """
    -------------------------------------------------------
    Returns the base price of the call
    Use: b_price = base_price(length)
    -------------------------------------------------------
    Parameters:
        length - number of minutes (int > 0)
    Returns:
        b_price - base price of the call (float)
    -------------------------------------------------------
    """
    price = length * 0.08
    return price


def time_discount(b_price , hour):
    """
    -------------------------------------------------------
    Returns the discount on time of the call
    Use: disc_t = time_discount(b_price , hour)
    -------------------------------------------------------
    Parameters:
        b_price - base price of call (float)
        hour - hour of call (int > 0)
    Returns:
        disc - discount on call for hour called
    -------------------------------------------------------
    """
    if(hour >= 18 and hour < 24):
        disc = b_price * 0.25
    elif(hour >= 0 and hour <= 8):
        disc = b_price * 0.50
    else:
        disc = 0
    return disc


def Length_discount(b_price , length):
    """
    -------------------------------------------------------
    Returns the discount on length of the call
    Use: disc_l = Length_discount(b_price , length)
    -------------------------------------------------------
    Parameters:
        b_price - base price of call (float)
        length - length of call (int > 0)
    Returns:
        disc - discount on call for length called
    -------------------------------------------------------
    """
    if(length >= 30):
        len_disc = b_price * 0.10
    else:
        len_disc = 0
    return len_disc
