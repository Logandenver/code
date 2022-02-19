#assignment 2

#You are given an integer N.
#You have to print number of prime numbers which are less than or equal to N

t=0
n=int(input())
for num in range(1,n):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            t+=1
print(t)