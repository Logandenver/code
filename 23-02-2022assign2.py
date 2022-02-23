#assignment 2
#program to print reverse of the elements in list
l=[]
n=int(input("Enter range: "))
for i in range(1,n+1):
    x=int(input())
    l.append(x)

l.reverse()
print("reversed list is: ",l)
    