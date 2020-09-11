"""
------------------------------------------------------------------------
Funtions for lab 7
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------
"""
from random import randint
def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    t=0
    while(t!=9):
        value=int(input('Enter a value between 0 and high 100:'))
        if(value<=low):
           print('Value entered is too low') 
           
        elif(value>=high):
            print('Value entered is too high')
        elif(value>=low and value<=high): 
            t=9   
            return value

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """


    number=randint(1,high)
    guess=int(input('Guess:'))
    count=1
    while(guess!=number):
        if(guess>number):
            print('Too high, try again.')
        
        elif(guess<number):
            print('Too low, try again.')
        
        guess=int(input('Guess:'))
        count+=1
        
    print('Congratulations - good guess!')
    
    return count        

def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """      
    
    
    cur_pop=current
    count=0
    
    while(cur_pop<target):
        cur_pop=cur_pop*(rate/100) + cur_pop
        count+=1
        
    return count
        
        
def positive_statistics():
    """


    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    total=0
    count=0
    curr=float(input('First positive value'))
    maxi=curr
    mini=curr
    while curr >= 0 :
        
        if maxi<curr :
            maxi=curr
        elif mini>curr:
            mini=curr
    
        total+=curr
        count+=1
        curr=float(input('Next positive value:'))
        
    average=total/count
    
    return mini,maxi,total,average

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0
    i = 1
    char = 'N'
    while(1):
        print("For Day {} \n".format(i))
        breakfast = float(input("How much was breakfast? $"))
        lunch = float(input("How much was lunch? $"))
        supper = float(input("How much was supper? $"))
                    
        b_total += breakfast
        l_total += lunch
        s_total += supper
        a_total += breakfast + lunch + supper 
        i += 1
        char = input("\nWere you away another day (Y/N)? ")
        if(char == 'Y'):
            continue
        else:
            break
    return b_total, l_total, s_total, a_total

          
          
    
    
            
    
        
    