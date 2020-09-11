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

seconds=int(input("Enter number of seconds:"))
hours=seconds//3600

minutes=(seconds//60)-(hours*60)
sec=seconds%60

print("There are {} hours, {:.0f} minutes, and {:.0f} seconds in {:.0f} seconds ".format(hours,minutes,sec,seconds))