"""
------------------------------------------------------------------------
Program 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-09"
------------------------------------------------------------------------
"""


from a7_functions import win_game

wingame = win_game()

print("Number of \"red\" entered: {}".format(wingame[0]))
print("Number of \"green\" entered: {}".format(wingame[1]))

if(wingame[0] > wingame [1]):
    print("\"red\" team wins!!!")
elif(wingame[0] < wingame[1]):
    print("\"green\" team wins!!!")
else:
    print("Tie!!!")
    