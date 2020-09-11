"""
------------------------------------------------------------------------
Lab 3 Question 9
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
PI=3.14

dia=float(input('Diameter of container base (cm): '))

height=float(input('Height of container (cm): '))

cost=float(input('Cost of material ($/cm^2): '))

containers=int(input('Number of containers:'))

area= (2*PI*(dia/2)*height) + ( PI*(dia/2)**2)

one_containers=float(area*cost)

all_containers=float(cost*containers*area)
print('')

print('The cost of one container is: ${:.2f}'.format(one_containers))

print('The total cost of all containers is ${:.2f}'.format(all_containers))