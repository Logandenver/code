#assignment 1
#program to print sum of even numbers and odd numbers
n=int(input("Enter number: "))
s1=0
s2=0
for i in range(2,n+1,2):
    s1=s1+i
    
for p in range(1,n+1,2):
    s2=s2+p

print("sum of even no's: ",s1)#optional
print("sum of odd no's: ",s2)#optional
print("sum of even and odd no's: ",s1+s2)
    
