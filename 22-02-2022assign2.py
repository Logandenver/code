#assignment 2
#program to print number series in a pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if i<5:
            print(j,end=" ")
    if j<4:
        print("\n")
print("\n")
for k in range(n-1,0,-1):
    for l in range(2,k+1):
        l-=1 
        print(l,end=" ")
    print("\n")

            
            
