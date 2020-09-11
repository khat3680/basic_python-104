print("Input your height: ")
h_inch = int(input("inches: "))
h_mete = int(input("meters: "))

h_mete += h_inch * (10000/254)

print("Your height is :" %h_mete)
