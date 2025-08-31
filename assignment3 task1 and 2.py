# Task 1
def fact(n):
    if n<0:
        return "no nagative value"
    elif n<2:
        return 1
    else:
        return n*fact(n-1)
    
value=int(input("Enter a number: "))

result = fact(value)

print('Factorial of',value,'is :',result)

#task 2

import math

num = int(input("Enter a number: "))
root = math.sqrt(num)
log = math.log(num)
sin = math.sin(num)
print("Square root:",root)
print("Logarithm:",log)
print("Sine:",sin)





