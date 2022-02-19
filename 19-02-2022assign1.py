#assignment 1
q=0
x=int(input("X : "))
y=int(input("y : "))
for num in range(x,y+1): 
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
            q+=1
print("count: ",q)

    
