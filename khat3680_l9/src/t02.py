"""
------------------------------------------------------------------------
Program 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

from functions import url_categorize

url = input("Enter the website address: ")

url_type = url_categorize(url)

print("{}".format(url_type))
