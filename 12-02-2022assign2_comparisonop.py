#assignment 2
#program to do comparison operations on operands
print("Enter the values: ")
a=int(input("a: "))
b=int(input("b:"))

if a==b:
    print("a and b are equal")
elif a!=b:
    print("a and b are not equal")
    if a>b:
        print("a is greater than b")
        print("b is smaller than a")
    elif a<b:
        print("a is less than b")
        print("b is greater than a")
    