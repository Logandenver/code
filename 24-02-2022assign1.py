#assignment 1
#to print count of prime numbers in a list
n=int(input("Enter range of list: "))
lst=[]
prime_list=[]
count=0
for q in range(1,n+1):
    lst.append(q)

for num in lst:
    if num>1:
        for j in range(2,num):
            if (num%j)==0:
                break
        else:
            count=count+1
            prime_list.append(num)
            
print("prime numbers are: ",prime_list)
print("count of prime numbers: ",len(prime_list))