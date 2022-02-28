#assignment 1
#to print 
n=int(input("enter range: "))
arr=[]
cnt=[]
for i in range(1,n+1):
    a=int(input())
    arr.append(a)
for c in arr: #upon traversing, we get duplicates upon checking of count of every number
    if ((arr.count(c))%2)==1:
        cnt.append(c)
new=[] #to remove duplicates, im using new list
[new.append(i) for i in cnt if i not in new] #list ccomprehension
print(new)