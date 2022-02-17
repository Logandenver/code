#assignment 2
#program to calculate n number of Fibonacci series
a=-1
b=1
n=int(input("Enter count: "))
for i in range(1,n+1):
    c=a+b
    print(c)
    a=b 
    b=c
