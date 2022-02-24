#assignment 2
#to seperate odd and even numbers from a list
n=int(input("enter range: "))
l=[]
even=[]
odd=[]
for i in range(1,n+1):
    l.append(i)   #or you can use a=int(input);l.append(a) # if you want to input data

for num in l:
    if num%2==0:
        even.append(num) 
    else:
        odd.append(num)

print("odd numbers: ",odd)
print("even numbers: ",even)