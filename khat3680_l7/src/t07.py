"""
------------------------------------------------------------------------
Program 7
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------
"""

from functions import meal_costs

b_total, l_total, s_total, a_total = meal_costs()

print("\nTotal: ")
print("Breakfast:   $ {:.2f}".format(b_total))
print("Lunch:       $ {:.2f}".format(l_total))
print("Supper:      $ {:.2f}\n".format(s_total))
print("Grand total: ${:.2f}".format(a_total))