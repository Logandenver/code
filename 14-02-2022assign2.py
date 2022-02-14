#assignment 2
#program to calculate sum of numbers in given numbers
a=int(input("Enter number: "))
b=a
result=0
while a>0:     #let num 985
    rem=a%10 # rem = 5
    result=result+rem #result = 0+5 = 5
    a=int(a/10) #a=98
print("Sum of all digits of ",b,"is: ",result)

    