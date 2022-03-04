#assignment 1
l=[]
n=int(input("range: "))
for i in range(1,n+1):
    a=int(input())
    l.append(a)
new=[]
for i in l:
    if i not in new:
        new.append(i)
count=(len(l))-(len(new))
print(count)
    