#assignment 1
n=int(input("range: "))
a=[]
neg=[]
pos=[]
for i in range(1,n+1):
    d=int(input(""))
    a.append(d)

for num in a:
    if num<0:
        neg.append(num)
    elif num>0:
        pos.append(num)
print("\n")
print("sorted list: ",pos+neg)


