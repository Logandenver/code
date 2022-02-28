#assignment 2
n=int(input("enter range: "))
arr=[]
for i in range(1,n+1): #using scanner method 
    a=int(input());
    arr.append(a)
arr1=[]
for num in arr:
    if ((arr.count(num)))==1:
        arr1.append(num)

print(arr1)
        
    
