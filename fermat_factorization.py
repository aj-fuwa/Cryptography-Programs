'''
# Das Ziel des Programms: Implementing Fermat's Method for factorization
# Date: 11.Juni 2020
# Die Sprache des Programms: Python
'''
import math as math
########################################################################################################################
# Step 1: Input the number n
n = int(input("Input the number to be factorised (Fermat's Method): "))
########################################################################################################################
# Step 2: Find x and y
index = 1
x = 0
flag = False    # will be set to True if number entered is not prime
                # else it will be False, if the number entered is prime
while(True):
    y = math.sqrt(n + math.pow(index, 2))

    if (y.is_integer()):    # type of y is float technically but the number is checked
        flag = True         # set to True since factors found
        x = index
        break

    index = index + 1

print("Values of x and y are: x=", x," y=", y)
########################################################################################################################
# Step 3: Find the factors f1 and f2
f1 = math.fabs(x - y)
f2 = math.fabs(x + y)
print("Factors are: ", f1, "and ", f2)
