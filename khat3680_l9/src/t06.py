"""
------------------------------------------------------------------------
Program 6
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
from functions import is_palindrome

s = input("Enter a string: ")

palindrome = is_palindrome(s)

if(palindrome == True):
    print("'{}' is  a palindrome".format(s))
else:
    print("'{}' is not a palindrome".format(s))
    
