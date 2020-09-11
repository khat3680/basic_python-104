"""
------------------------------------------------------------------------
Functions for programs
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-22"
------------------------------------------------------------------------
"""

#def sum_numbers():

def find_median(fv):
    """
    -------------------------------------------------------
    Find the median of the group of scores into a list.
    Use: result = find_median(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        result - the median of the list (number)
    -------------------------------------------------------
    """
    result = ''     
    list_1=[]
    lin_n=fv.readline()
    list_1=lin_n.strip().split(' ')

    
    for lin_n in fv :
          
        list_2=lin_n.strip('\n').split(' ')
        
        list_1=list_1 + list_2 
    del list_1[-4]
    
    
    for i in range(0,len(list_1),1):    
        list_1.sort()
        if len(list_1)%2==0 :
            result = list_1[int(len(list_1)/2)] + list[int(len(list_1)/2) +1 ]
        else:
            result= list[int(len(list_1)/2) +1 ]    
    print(list_1)        
            
    
           
    return result
    
    