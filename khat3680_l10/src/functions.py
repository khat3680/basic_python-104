"""
------------------------------------------------------------------------
Functions for Program 
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-20"
------------------------------------------------------------------------
"""

def customer_record(fv, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fv, n)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result=[]
    i =-1
    if n>4 :
        result=[]
    else:    
        while i<=n :
            line_n=fv.readline()
            line_n=line_n.rstrip('\n').split(',')
            i=i+1
            if i==n :
                result =line_n    
    return result   


def customer_best(fv):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    result = []      
    maxi = -1

    line_n =fv.readline()  
    while line_n != '' :
        cur_customer = line_n.strip().split(',')
    
        if float(cur_customer[3]) > float(maxi) :
            maxi = float(cur_customer[3])
            result = cur_customer
            
        line_n=fv.readline()
            
               
    return result

def append_increment(fv):
    """
    -------------------------------------------------------
    Appends a number to the end of the fv. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    num = 0
    line = fv.readline()
    while line != "":
        num1 = int(line)
        line = fv.readline()
    num = num1 + 1
    fv.write("{}\n".format(num))
    
    return num

def count_frequency_value(fv, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fv.
    Use: count = count_frequency_value(fv, value)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fv (int)
    ------------------------------------------------------
    """
    count = 0
    for i in fv:
        if int(i) == value:
            count += 1
            
    return count


def file_copy_n(fv_1, fv_2, n):
    """
    -------------------------------------------------------
    Copies n record from fv_1 (starting from the beginning of the file) to fv2
    Use: file_copy_n(fv_1, fv_2, n)
    -------------------------------------------------------
    Parameters:
        fv_1 - file to search (file - open for reading)
        fv_2 - file to search (file - open for appending)
    Returns:
        None
    ------------------------------------------------------
    """
    i=1
    line=fv_1.readline()
    if  line!='' :
        fv_2.write(line)
    while i<n and line!='':
        line=fv_1.readline()
        
        fv_2.write(line)
        i=i+1
    return None