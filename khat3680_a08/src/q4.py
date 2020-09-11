"""
------------------------------------------------------------------------
Program 4
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-14"
------------------------------------------------------------------------
"""
from a8_functions import is_word_chain
n=int(input('Enter the number of animals\n'))
list_animals=[]

for i in range(n):
    animals=(input('Enter the name of animal\n'))
    list_animals.append(animals)


print(list_animals)

ani_=is_word_chain(list_animals)
print(ani_)

