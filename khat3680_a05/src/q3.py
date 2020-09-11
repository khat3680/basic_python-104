"""
------------------------------------------------------------------------
 Program 3
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-11"
------------------------------------------------------------------------
"""
from a3_functions import Length_discount
from a3_functions import base_price
from a3_functions import time_discount

length = int(input("Length of call (minutes): "))
hour = int(input("Hour of call (24 hour format): "))

b_price = base_price(length)

disc_time = time_discount(b_price, hour)

disc_length = Length_discount(b_price, length)

total_answer = b_price - (disc_time + disc_length)
print()

print("Total price of call: ${:.2f}".format(total_answer))
