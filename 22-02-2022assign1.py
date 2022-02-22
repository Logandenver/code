#assignment 1
#program to print pyramid diamond shape
n=int(input())
for i in range(1,n):
    print(" "*(n-i-1),end=" ")
    for j in range(0,i):
        print("*",end=" ")
    if j<4:
        print("\n")
for k in range(n-1-1,0,-1):
    print(" "*(n-k-1),end=" ")
    for t in range(1,k+1):
        print("*",end=" ")
    print("\n")