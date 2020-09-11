"""
------------------------------------------------------------------------
Program Description
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

number =float(input("Enter number: "))
percent =float(input("Enter percent: "))
answer=(percent/100)*number
print("A ",percent,"percent discount on","{:.1f}".format(number),"is","{:.1f}".format(answer))
print("A {} percent discount on {:.1f} is {:.1f}".format(percent, number, answer))
