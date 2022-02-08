#Assignment 1
#program to perform all comparison operations
#comparison operators are mostly used with conditional statements (if else) 
a=int(input("enter a value:"))
b=int(input("enter b value:"))
#using < and > operators
if a>b:
    print("a is Big")
elif a<b:
    print("b is big")
#using == and != operators
elif a==b:
    print("a and b values are equal")
elif a!=b:
    print("a is not equal to b, opposite values")
#using <= and >= operators
elif a<=b:
    print("a is less than or equal to b")
elif a>=b:
    print("a is greater than or equal to b")
#here we wont get <= or >= results because we already have == operator condition

#for example, lets use < and > operator to perform a weather report program
w=float(input("enter temperature in degree"))
if w<=10:
    print("weather is too cold,it's",w,"degrees,stay warm")
elif w>10 and w<=30:
    print("weather is moderately cool,it's",w,"degrees,stay cozy")
elif w>30 and w<=45:
    print("weather is moderate and dry,it's",w,"degrees,enjoy the sun and beautiful weather")
else:
    print("weather is HOT,it's",w,"degrees, be hydrated and cool")


    



