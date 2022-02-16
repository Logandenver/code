def is_leap(year):
    leap = False
    leap2= True
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return leap2
    else:
        return leap

year = int(input())
print(is_leap(year))