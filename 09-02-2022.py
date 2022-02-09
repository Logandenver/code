#assignment 1
#program to print biggest of two numbers
#receiving input using scan function
print("---------Check biggest of two numbers---------")
a=input("enter a value: ")
b=input("enter b value: ")
if a>b:
    print("a is biggest number")
else:
    print("b is biggest number")

#another method
c=input("enter a value: ")
d=input("enter b value: ")
if c<d:
    print(c,"is bigger number")
elif c>d:
    print(d," is bigger number")
#using elif i can give multiple conditions and its not mandatory to have else.

