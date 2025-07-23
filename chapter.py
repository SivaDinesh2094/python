#task1

number=int(input("Enter a number:"))
result=number%2

if(result==0):
    print(number,"is an even number")
else:
    print(number,"is an odd number")


#task2

number=list(range(0,51))
sum=0
for i in number:
    sum=sum+i
print("The sum of number from 1 to 50 is :",sum)
