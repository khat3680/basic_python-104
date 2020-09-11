"""
------------------------------------------------------------------------
Lab 5 Question 9 
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
"""

from functions import wind_speed

speed = int(input("Wind speed (km/h): "))

category = wind_speed(speed)

print("Category: {}".format(category))

