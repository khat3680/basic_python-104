"""
------------------------------------------------------------------------
Assignment 4 Function module
Question 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-03"
------------------------------------------------------------------------
"""

def calc_federal_tax(income):
    
    """

    -------------------------------------------------------

    Calculates fedral tax 

    Use: fedtax = calc_fedral_tax(income)

    -------------------------------------------------------

    Parameters:

       income- Takes the income of he user as parameter

    Returns

        fed - Returns the final calculated over the total tax 

    -------------------------------------------------------

    """


    TAX_=35000*0.15
    TAX_2=65000*0.25
    above=income-(100000)
    tax_3= above*0.35
    fed = TAX_ + TAX_2 + tax_3
    return fed
    

def calc_prov_tax(income):
    """

    -------------------------------------------------------

    Calculates fedral tax 

    Use: fedtax = calc_prov_tax(income)

    -------------------------------------------------------
     
    Parameters:

       income- Takes the income of he user as parameter

    Returns

        pro - Returns the final calculated over the total tax 

    -------------------------------------------------------

    """
    
    sal=income-50000
    pro=sal*0.05
    return pro
