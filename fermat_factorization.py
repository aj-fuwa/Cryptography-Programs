'''
# Das Ziel des Programms: Implementing Fermat's Method for factorization
# Date: 11.Juni 2020
# Die Sprache des Programms: Python
'''
import math as math
import sympy as sp          # python library for symbolic mathematics
########################################################################################################################
# Step 1: Input the number n
n = int(input("Input the number to be factorised (Fermat's Method): "))

if (sp.isprime(n)): # if the number is prime, then exit
    print("Number entered:", n, "is prime. No factors!")
    exit()
########################################################################################################################
# Step 2: Find x and y
index = 1
x = 0

while(True):
    y = math.sqrt(n + math.pow(index, 2))

    if (y.is_integer()):    # type of y is float technically but the number is checked
        x = index
        break

    index = index + 1

print("Values of x and y are: x=", x," y=", y)
########################################################################################################################
# Step 3: Find the factors f1 and f2
f1 = math.fabs(x - y)
f2 = math.fabs(x + y)

print("Factors are: ", f1, "and ", f2)

