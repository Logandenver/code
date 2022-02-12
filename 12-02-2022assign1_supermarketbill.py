#assignment 1
#program to generate a super market bill
print("-------Welcome to DMart--------")
print("\n-------- billing details--------")
name=input("Customer name: ")
print("item                     price")
p1=float(input("Amul Milk 200ml:        "))
p2=float(input("hershey's syrup 400ml:  "))
p3=float(input("gooday chocochip 5pack: "))
p4=float(input("Kissan Ketchup 500ml:   "))
p5=float(input("candyman 2x pack:       "))

t=p1+p2+p3+p4+p5 #t is total
print("\ntotal:  ",t)

if t>5000:
    t=t-(t*(10/100))
    print("Discount: 10%")
elif t>3000 and t<5000:
    t=t-(t*(8/100))
    print("Discount: 8%")
elif t>2000 and t<3000:
    t=t-(t*(5/100))
    print("Discount: 5%")
elif t>1000 and t<2000:
    t=t-(t*(3/100))
    print("Discount: 3%")

if t>3000:
    t=t+(t*(10/100))
    print("Tax: 10%")
else:
    t=t+(t*(18/100))
    print("Tax: 18%")

print("Net amount: ",t)

print("\nAmount Payable: ",t)
