"""
------------------------------------------------------------------------
ASSIGNMENT 3 ; QUESTION 4
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-26"
------------------------------------------------------------------------
"""

def calorie_calculator(grams_fat,grams_carb):
    '''
----------------------------------------------------------
    Calculates the total calorie of fat and carb
    use: fat=grams_fat*9, carb=grams_carb*4
---------------------------------------------------------- 

Parameters 
    grams_fat=.Returns:
    fat
    '''
    
    calories_fat=(grams_fat)*9
    
    calories_carb=(grams_carb)*4
    
    return (calories_fat,calories_carb)
    

grams_fat= float(input('Enter the fat grams consumed: '))
grams_carb=float(input('Enter the carbohydrate grams consumed: '))
print()
grams_fat,grams_carb = calorie_calculator(grams_fat, grams_carb)
TOTAL = grams_carb+grams_fat

print('Total calories a total of {:.0f}[Fat calories:{:.2f} and Carb calories: {:.2f}]'.format(TOTAL,grams_fat,grams_carb))



