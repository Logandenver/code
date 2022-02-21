n=int(input("Enter range: "))
ascii=97
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(ascii),end=" ")
        ascii+=1
    print("\n")