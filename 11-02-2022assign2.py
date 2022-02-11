#assignment 1
#program to generate student result
print("---------STUDENT RESULT---------")

print("\nEnter your details: ")
sno=int(input("student number: "))
name=input("student name: ")
group=input("enter your group: ")

print("\nenter your subject marks: ")
os=float(input("operating system: "))
java=float(input("OOPS using JAVA: "))
acc=float(input("accounting and finanical management: "))
eng=float(input("english: "))
tel=float(input("telugu: "))
ob=float(input("online business: "))

total=os+java+acc+eng+tel+ob 
avg=total/2

if (os or java or acc or eng or tel or ob)<35:
    print("\nFail")
    print("Grade : F")
else:
    if avg>=91:
        print("\nGrade : O")
    elif avg>=81 and avg<91:
        print("\nGrade : A")
    elif avg>=71 and avg<81:
        print("\nGrade : B")
    elif avg>=61 and avg<71:
        print("\nGrade : C")
    elif avg>=51 and avg<61:
        print("\nGrade : D")
print("Pass")
    