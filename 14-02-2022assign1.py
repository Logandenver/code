#assignment 1
#program to calculate number of digits in a given number

x = int(input("User Input: "))
c = 0 #c is the count of digit
while x > 0:
   x = int(x/10)
   c += 1 
print("Number of Digits: ",count_of_digits)