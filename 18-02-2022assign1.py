#assignment 1
#program to print count of n prime numbers
n=int(input("Enter count: "))
for n in range(1,n+1):
    if n>1:
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            print(n)
