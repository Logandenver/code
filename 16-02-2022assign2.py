def is_leap(year):
    leap = False
    leap2 = True
    if (year%4==0)or(year%100!=0):
        return leap
    else:
        return leap2

year = int(input())