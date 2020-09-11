"""
------------------------------------------------------------------------
Program Description
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2020-1-3"
------------------------------------------------------------------------
"""

def list_fun():
    square_=[]
    for i in range(1,21):
        square_.append(i**(2))
    print(square_[-5:])
#print(list_fun())

def email_veri(email):
    d=[]
    d=email.split("@")
    
    