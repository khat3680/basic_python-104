"""
------------------------------------------------------------------------
Functions for Programs
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-27"
------------------------------------------------------------------------
"""

import random
 
def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    
    matrix = []
    
    for i in range(rows):
        d_list=[]
        for j in range(cols):
           
            if value_type == 'float' :
                
                t=random.uniform(low,high)
                d_list.append(t)
            
            elif value_type == 'int' :
                    
                    t = random.randint(low,high)
                    d_list.append(t)
            else:
                t=random.randint(low,high)
                d_list.append(t)

                    
    
        matrix.append(d_list)    
    return matrix     


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])
    print(" ", end="")
    for i in range(cols):
        print("{:7}".format(i), end="")
    print()
    for i in range(rows):
        print("{:2}".format(i), end="")
        for j in range(cols):
            if value_type == "float":
                print("{:7.2f}".format(matrix[i][j]), end="")
            if value_type == "int":
                print("{:7}".format(matrix[i][j]), end="")
        print()

    return 
    


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    s_loc = [0,0]
    l_loc = [0,0]
    big = matrix[0][0]
    small = matrix[0][0]
    for i in  range(len(matrix)):

        for j in  range(len(matrix[i])):
            if small >matrix[i][j] :
                small=matrix[i][j]
                s_loc=[i,j]
                
            if big < matrix[i][j]:
                big=matrix[i][j]

                l_loc=[i,j]
                
    return s_loc,l_loc
        
def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    
    for i in range(rows):
        
        for j in range(cols):
            
                matrix[i][j]=num*matrix[i][j]
        
    return None


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of ?)
        matrix2 - the second matrix (2D list of ?)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    rows = len(matrix1)
    cols = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if rows==rows2 and cols==cols2 :
        
        for i in range(rows):
        
            for j in range(cols):
            
                if  matrix1[i][j]==matrix2[i][j]:
                    equal=True
                else:
                    equal=False
    else:
        
        equal=False
        
    return equal
