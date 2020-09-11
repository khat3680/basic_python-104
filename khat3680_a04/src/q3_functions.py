"""

------------------------------------------------------------------------
Assignment 4 Question 3 
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
def num_day(day_int):
    """
    -------------------------------------------------------

    Calculates the average for three quiz scores

    Use: avg = num_day(day_int)

    -------------------------------------------------------

    Parameters:

        day_int // for number coressponding to day

    Returns

        day and error message as string

    -------------------------------------------------------

    """

   


    if(day_int==1):
        return 'Monday'
    if(day_int==2):
        return 'Tuesday'
    if(day_int==3):
        return 'Wednesday'
    if(day_int==4):
        return 'Thursday'
    if(day_int==5):
        return 'Friday'
    if(day_int==6):
        return 'Saturday'
    if(day_int==7):
        return 'Sunday'
    
    elif(day_int > 7 or day_int < 1 ):
        return'Sorry,that is not a valid number '
    