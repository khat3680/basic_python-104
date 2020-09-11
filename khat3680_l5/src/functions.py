"""
------------------------------------------------------------------------
Function Module
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-10"
------------------------------------------------------------------------
"""

def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg) ◊ acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        newtons - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    ACC = 9.8
    newtons = float(mass * ACC)
    
    if(newtons < 10):
        message = "light"
    elif(newtons > 1000):
        message = "heavy"
    else:
        message = "average"
        
    return (newtons, message)

def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0) 
    Returns:
        result - True if year is a leap year,
            False otherwise (bool)
    ------------------------------------------------------
    """
    if(year % 100 == False):
        if(year % 400 == False):
            result = True
        else:
            result = False
    elif(year % 4 == False):
        result = True
    else:
        result = False
    return result

def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if speed < 0:
        category =  "Unknown"
    elif speed < 39:
        category =  "Breeze"
    elif speed < 62:
        category =  "Strong Wind"
    elif speed < 89:
        category =  "Gale Winds"
    elif speed < 118:
        category =  "Whole Gale"
    else:
        category =  "Hurricane"
    return category

def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (bool)
    -------------------------------------------------------
    """
    YEARS = 5
    SAL = 30000
    YEARS_EMPLOYED = int(input("Years employed: "))
    
    if(YEARS_EMPLOYED >= YEARS):
        SALARY = int(input("Annual salary: "))
        if(SALARY >= SAL):
            qualified = True
        else:
            qualified = False
    elif(YEARS_EMPLOYED < YEARS):
        qualified = False
    else:
        qualified = False
    return qualified
def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
        
    B = 6
    F = 1.50
    S = 2
    W = 8
    
    total=0
    order=input('Order B - burger or W - wings:')
    if(order=='B'):
        combo=input('Make it a combo?(Y/N)')
        if(combo=='Y'):
            sec_th=input('Add F - fries or S - salad:')
            total = B +  
'''
ORDER1 = input("Order B - burger or W - wings: ")
    
    if(ORDER1 == "B"):
        COMBO = input("Make it a combo? (Y/N): ")
        if(COMBO == "Y"):
            CHOICE = input("Add F - fries or S - salad: ")
            if(CHOICE == "F"):
                price = B + F
            else:
                price = B + S
        else:
            price = B
    else:
        COMBO = input("Make it a combo? (Y/N): ")
        if(COMBO == "Y"):
            CHOICE = input("Add F - fries or S - salad: ")
            if(CHOICE == "F"):
                price = W + F
            else:
                price = W + S
        else:
            price = W
            
    return price
    '''
        

