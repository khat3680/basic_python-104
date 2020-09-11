"""
------------------------------------------------------------------------
Assignment 4 Function module
Question 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from random import randint
def math_quiz ():
    """
    -------------------------------------------------------

    Calculates the sum of random number and checks for the user

    Use: math_quiz():

    -------------------------------------------------------

    Parameters: none
    Returns: none

    -------------------------------------------------------

    """

    
    a=randint(0,999)
    b=randint(0,999)
    print('  {}'.format(a))
    print('+ {}'.format(b))
    final=a+b
    print()
    answer=int(input('Answer : '))
    print()
    if (answer==final) :
        print('Congratulations, correct answer!')
    else:
        print('Incorrect- The answer should be: {}'.format(final))
        
        
