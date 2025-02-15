"""
------------------------------------------------------------------------
Program Description
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-14"
------------------------------------------------------------------------
l=diameter(2.5)

print('Diameter of circle: {:.2f}'.format(l) )
b=float(input('Enter base'))
p=float(input('Enter height'))
print()
sh,a,v=square_pyramid(b ,p)

print('Slant height of square pyramid: {:.2f}'.format(sh))
print('Area of square pyramid: {:.2f}'.format(a))
print('Volume of square pyramid: {:.2f}'.format(v))

"""
from math import sqrt


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: d = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        d - diameter of a circle (float)
    ----
    """
    d=radius*2
    return d


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, a, v = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        a - area of the square pyramid (float)
        v - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    
    slant_h=float(sqrt( (base/2)**2 + height**2 ))
    area = base**2 + 2*base*slant_h
    volume=base**(2)*(height/3)
    
    return slant_h,area,volume    

def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    
    
    num=(num1*num2)
    den=den1*den2
    product=num/den
    return num,den,product

"""  
num1=float(input('Enter numerator of fraction 1:'))
den1=float(input('Enter denominator of fraction 1:')) 
num2=float(input('Enter numerator of fraction 2:')) 
den2=float(input('Enter denominator of fraction 2:'))

num,den,product=fraction_product(num1, den1, num2, den2) 


n=45455.456
print('{:78,.2f}'.format(n))
"""
def sum_odd(num):
    '''
    ------------------------------
    Sums the odd numbers from 1 to num (inclusive)
    use: sum_odd(num
    ------------------------------
    Parameters :
    num - an Integer  (int>0)
    ------------------------------
    Returns:
    total-an Integer
    ------------------------------
    '''
    total=0
    for i in range(1,num+1,2):
        total+=i
    return total

def sum_partial_harmonic(n):
    total=0
    for i in range(1,n+1,1):
        total+=1/i
    return total
'''
last_term=int(input('Enter a number'))
p=sum_partial_harmonic(last_term)
print('The sum of aprtial harmonic series from 1 to {} is {}'.format(last_term,p))
'''

def draw_triangle(height,char):
    for i in range(1,height+1,2):
        print('{8s}'.format(char))
            
height=int(input('Enter the height: '))
char_=input('Enter the symbol')
p=draw_triangle(height,char_)

