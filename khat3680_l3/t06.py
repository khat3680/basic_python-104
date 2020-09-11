"""
------------------------------------------------------------------------
Lab 3 Question 6
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""

principal_amt = float(input("Mortgage principal ($): "))
no_of_years = int(input("Number of years: "))
yearly_interest_rate = float(input("Yearly interest rate (%): "))

no_of_months = no_of_years * 12
monthly_interest_rate = (yearly_interest_rate / 12) / 100

MONTHLY_PAYMENT = principal_amt * ((monthly_interest_rate * (1 + monthly_interest_rate) ** no_of_months) / (((1 + monthly_interest_rate) ** no_of_months) - 1))

print("The monthly payments are: ${:,.2f}".format(MONTHLY_PAYMENT))

