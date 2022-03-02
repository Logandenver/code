row=int(input("enter row size: "))
col=int(input("enter col size: "))

matrix=[]
for i in range(row):
    r=[]
    for j in range(col):
        ele=int(input("enter values: "))
        r.append(ele)
    matrix.append(r)
    print("\n")
print(matrix)

matrix2=[]
for i in range(row):
    l=[]
    for j in range(col):
        ele=int(input("enter values: "))
        l.append(ele)
    matrix2.append(l)
    print("\n")
print(matrix2)

result=[[0 for i in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j] = matrix[i][j]-matrix2[i][j]

print("The Subtraction of Above two Matrices is : ")
for r in result:
    print(r)

    

            

