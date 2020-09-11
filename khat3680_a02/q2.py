"""
------------------------------------------------------------------------
Assignment 2 : Question 2
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-18"
------------------------------------------------------------------------
"""


p=float(input("Principal:"))
r=float(input("Interest (decimal):"))
t=float(input("Number of years:"))
n=float(input("Compound interest per year: "))
a=float( (p)*(pow( (1+ r/n),(n*t)) )  )

print("Balance: $",round(a,3))
      



