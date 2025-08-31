# Task 1
def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
    
value=int(input("Enter a number: "))

result = fact(value)

print('Factorial of',value,'is :',result)


''' Task 2'''




