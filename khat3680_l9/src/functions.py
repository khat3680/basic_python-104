"""
------------------------------------------------------------------------
Functions for lab 9
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-14"
------------------------------------------------------------------------
"""

def str_distance(s1, s2):

    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    count=0
    d=0
    if len(s1)==len(s2) :
        if s1==s2 :
            d= 0
        else:
            for i in range(len(s1)):
                count+=1
                if s1[i]==s2[i] :
                    break
        d=count   
    elif len(s1)!=len(s2):
        d= -1
    return d
def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    s = s.lower()
    t = s[::-1]
    palindrome = False
    if(s == t):
        palindrome = True
    else:
        palindrome = False
    return palindrome

def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    url_type = "other"
    if(url.endswith("com") == 1):
        url_type = "business"
    elif(url.endswith("org") == 1):
        url_type = "non-profit"
    else:
        url_type = "other"
    return url_type

def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """ 
    maketrans = s.maketrans 
    out = s.translate(maketrans(',', '.')) 
    return out



def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    
    first_part=product_code[0:3]
    second_part=product_code[3:7]
    third_part=product_code[7:]
    
    category_1='not valid'
    category_2='not valid'
    category_3='not valid'
    
    
    if len(first_part) <3 :
        print("Category is {}.".format(category_1))
        
    else:
            
        if first_part.islower() or first_part.isdigit():
            print("Category {} is {}.".format(first_part,category_1))
        else:
            category_1='valid'
            print("Category {} is {}.".format(first_part,category_1))
    
    if len(second_part) <4 :
        
        print("ID is {}.".format(category_2)) 
        
    else:
    
  
        if second_part.isdigit():            
            category_2='valid'
            print("ID {} is {}.".format(second_part,category_2))
            
        else:
            print("ID {} is  {}.".format(second_part,category_2))
            
    if len(third_part)==0 :
        
        print("Qualifier  is {}.".format(category_3))
    else:        
        if third_part[0].isupper():
            category_3='valid'
            print('Qualifier {} is {}'.format(third_part,category_3)) 
        else:
            print("Qualifier  {} is  {}.".format(third_part,category_3))
            
    return None   

