"""
------------------------------------------------------------------------
Program Description
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
Member 2: Homa Varmora
Member 3: Bahadir Unver
__updated__ = "2019-09-24"
------------------------------------------------------------------------
"""
# Function to subtract two numbers 
def subtraction (no1, no2):
    result = -(no2 - no1)
    print("Result log from subtraction: ", result)
    return result

# Function to add two numbers
def addition (no1, no2):
    result = no2 + no1
    print("Result from addition: ", result)
    return result

# Function to multiply two numbers 
def multiply(num1, num2): 
    result=num1 * num2 
    print("Result from multiplication: ", result)
    return result
# Function to divide two numbers 
def divide(num1, num2): 
    result=(num1)/ (num2)
    print("Result from division: ", result)
    return result
# Function to find remainder of two numbers 
def modulus (no1, no2):
    result = (no1)%(no2)
    print("Remainder is : ",result)
    return result

# Function to divide two number and gives result as whole number      
def intdiv (no1, no2):  
    result=no1//no2
    print("Result from division of two numbers as a whole number : ", result)
    return result      
    
    
def main():
    no1=int(input('Enter the 1st no.')) 
    no2=int(input('Enter the 2nd no.'))
    subtraction(no1, no2)
    addition(no1, no2)
    multiply(no1, no2)
    divide(no1, no2)
    modulus(no1, no2)
    intdiv(no1, no2)
    
main()
    
