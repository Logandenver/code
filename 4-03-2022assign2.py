#assignment 2
n=int(input("range: "))
l=[]
for i in range(1,n+1):
    a=int(input())
    l.append(a)

for i in range(1,n+1):
    max=0
    for j in l:
        if j>max:
            max=j
    n=0
    for k in l:
        if k>n and k<max:
            n=k
    c=0
    for m in l:
        if m>c and m<n:
            c=m 
print(c)

        