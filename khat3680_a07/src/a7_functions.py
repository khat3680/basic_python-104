"""
------------------------------------------------------------------------
Functions for Programs 
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

    
def win_game():
    """
    -------------------------------------------------------
    calculates and displays number of times red and green won
    Use: win = win_game()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        win - list of count of number of times red won and number of times green won (list)
    ------------------------------------------------------
    i used while loop because number of inputs were not defined
    ------------------------------------------------------
    """
    lists = []
    win = []
    counter = 0
    countr = 0
    countg = 0
    while(1):
        team = input("Enter \"red\" or \"green\" or press ENTER to stop: ")
        team = team.lower()
        if(team == ""):
            break
        elif(team == "red" or team == "green"):
            lists.append(team)
            counter += 1
        else:
            continue
    for i in range(0, counter, 1):
        if(lists[i] == "red"):
            countr += 1
        elif(lists[i] == "green"):
            countg += 1
        else:
            continue
    win.append(countr)
    win.append(countg)
    
    return win    


def display_pattern(num_lines):
    """
    -------------------------------------------------------
    displays pattern
    Use: display_pattern(num_lines)
    -------------------------------------------------------
    Parameters:
        num_lines - number of lines
    Returns:
        none
    ------------------------------------------------------
    """
    for i in range(num_lines):
        for j in range(num_lines):
            if(j == 0 or i == (num_lines - 1) or i == j):
                print("#", end='')
            else:
                print(end=' ')
        print()

        
def keep_positive_numbers():
    """
    -------------------------------------------------------
    makes a list of positive integers
    Use: list = keep_positive_numbers()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        list - a list of positive integers
    ------------------------------------------------------
    """
    lists = []
    while(1):
        try:
            number = int(input("Enter Number: "))
            if(number == 0):
                break
            elif(number > 0):
                lists.append(number)
            else:
                continue
        except:
            continue

    return lists


def find_value(lists, target):
    """
    -------------------------------------------------------
    takes a list of positive integers and the finds the value at target position and returns position
    Use: loc = find_value(list,target)
    -------------------------------------------------------
    Parameters:
        list - list of positive numbers (list)
        target - variable to find the location of (int > 0)
    Returns:
        loc - location(s) of the target (list)
    ------------------------------------------------------
    """
    loc = []
    l = len(lists)
    for i in range(0, l, 1):
        if(lists[i] == target):
            loc.append(i)
        else:
            continue
    return loc
    