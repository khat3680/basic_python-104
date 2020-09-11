"""
------------------------------------------------------------------------
Functions for Lab 8
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-04"
------------------------------------------------------------------------
"""
from random import randint
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    try:
        month_list = ["Sunday", "Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = month_list[d - 1]
    except:
        day = "Invalid Day"
    return day

def get_lotto_numbers(n,low,high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    list_1 = []
    for i in range(0, n):
        number = randint(low, high)
        found = number in list_1
        while found==True :
            number = randint(low, high)
            found = number in list_1
        list_1.append(number)
               
    return list_1

def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    User: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """
    index = -1
    i = 0
    q = len(a)
    found = v in a
    if(found == 0):
        index = -1
    else:
        while(q):
            if(a[i] == v):
                index = i
                break
            else:
                index = -1
            i += 1
    return index

def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sum(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    final = []
    for i in range(len(source1)):
        final.append(source1[i] + source2[i])
    return final

def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    
    target=[]
    for i in range(len(source1)):
        if source1[i] not in source2 and source1[i] not in target :
            target.append(source1[i])
    for j in range(len(source2)):
        if source2[j] not in source1 and source2[j] not in target :
            target.append(source2[j])
    return target


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    name_dig=['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
    for i in range(len(name_dig)):
        if i==n :
            name=name_dig[i]
    return name 

Dec=123.323
print('{1:.1s}'.format((Dec),('Hello')))













