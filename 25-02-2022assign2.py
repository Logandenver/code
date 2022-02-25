#assignment 2
n=int(input("Enter range: "))
lst=[]
lst2=[]
count=0
for i in range(1,n+1):
    a=int(input())
    lst.append(a)

for z in lst:
    if z!=0:
        lst2.append(z)
        count=count+1
print("\n")
print("count of non zero elements: ",count)
print("non-zero elements are: ",lst2)
        
        
