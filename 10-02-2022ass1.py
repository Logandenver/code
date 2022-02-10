#assignment 1
#program to generate a student result whether pass or fail
print("-------Kindly Enter your details------")
Rno=int(input("roll number: "))
group=input("group: ")
regno=int(input("register number: "))
print("-------Enter your subject marks-------")
java=float(input("Java: "))
acc=float(input("accounts: "))
os=float(input("operating system: "))
tel=float(input("Telugu: "))
eng=float(input("english marks: "))
ob=float(input("online business marks: "))
ee=float(input("environmental education: "))
if (java and acc and os and tel and eng and ob and ee)>35:
    print("Grade: Pass\n-----Well done-----")
else:
    print("Grade: Fail\n-----better luck next time-----")
