"""
------------------------------------------------------------------------
Program 1
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------


from functions import hi_lo_game

max_1=int(input('Enter the maximum value you want numbers to:'))

no_guess=hi_lo_game(max_1)

print('You made {} guesses'.format(no_guess))

#print('I\'m going there')

#print("Mon\tTue\tWed\tThu\tFri")
#print("Rain\tSun\tSun\tSun\tRain")

#print("\n\n\n\n\n\n\n")
#print("Program ends")


score = 0.56
print(format(score, '%'))
print(format(score, '.2%'))
print(format(score, '.0%'))
print("\n")
print(format(123456, ',d'))
print(format(12345.6, '15,'))
print('{:,d}'.format(1000000))

for i in range(5,-1,-1):
    print(i)
    """
n=5.4
#print(format(123456, ','))
print('{:8.2f}'.format(n))
