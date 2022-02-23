#assignment 1
#program to print maximum and minimum elements from the list
list=[]
n=int(input("Enter range of list: "))
for i in range(1,n+1):
    a=int(input())
    list.append(a)

print("finding max and min values using a loop: ")
maxi=list[0]
for m in list:
    if m>maxi:
        maxi=m
print("maximum value in list is: ",maxi)


mini=list[0]
for n in list:
    if n<mini:
        mini=n 
print("minimum value in list is: ",mini)
print("\n")

#using list methods
print("finding max and min values using list methods: ")
print("maximum value: ",max(list))
print("minimum value: ",min(list))


    