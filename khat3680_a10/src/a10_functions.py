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


def add_matrices(list1,list2):
    """
    -------------------------------------------------------
    adds the two matrices
    Use: sum = add_matrices(list1, list2)
    -------------------------------------------------------
    Parameters:
        list1 - first matrice (2D list)
        list2 - second matrice (2D list)
    Returns:
        sum - the sum of the two matrices (2D list)
    -------------------------------------------------------
    """
    sum_1 = [] 
    for i in range(len(list1)):
        row = []
        for x in range(len(list1[i])):
            row.append(list1[i][x] + list2[i][x])
        sum_1.append(row)
 
    return sum
 

def largest_even(list):
    """
    -------------------------------------------------------
    finds the maximum even value in the list
    Use: max_even = largest_even(list)
    -------------------------------------------------------
    Parameters:
        list - list of integers (2d list)
    Returns:
        max_even - the maximum even value in list (int)
    -------------------------------------------------------
    """
    max_even = 1
    for i in range(len(list)):
        for x in range(len(list[i])):
            if list[i][x]>max_even and list[i][x]%2==0:
                max_even = list[i][x]
    return max_even

list_=[5,3,9,2,10]
 
def min_diff(list_):
    min_n=0
    for i in range(len(list_)):
        for j in range (i):
            diff=list_[i]-list_[j]
            neg= (-1)*min_n
            if min_n > diff or neg > diff :
                min_n=diff
    print(min_n)
min_diff(list_)


def word_freq(str):
    """
    -------------------------------------------------------
    Creates a dictionary based on the words
    Use: dict = words_freq(str)
    -------------------------------------------------------
    Parameters:
        str - input by the user (string)
    Returns:
        dict - the number of times each word shows up (dictionary)
    -------------------------------------------------------
    """
    words = str.split()
    list_1 = []
    done = []
    dict_ = {}
   
    for i in words:
        row = []
        if i not in done:
            row.append(i)
            done.append(i)
            row.append(words.count(i))
            list_1.append(row)
   
    for i in range(len(list)):
        for x in range(1):
            dict_[list_1[i][x]] = list_1[i][x+1]
   
    return dict_