"""
------------------------------------------------------------------------
Program 8
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""
from functions import append_increment

fv = open("numbers.txt", "r+", encoding="utf-8")

num = append_increment(fv)

print("file 'numbers.txt' open for reading and writing")
print("{} is appended".format(num))

