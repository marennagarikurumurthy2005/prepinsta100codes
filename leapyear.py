""" x = int(input("Enter Year: "))

if x % 4 == 0:                 
    if x % 100 != 0:            
        if x % 400 != 0:        
            print(x, "is a Leap Year")
        else:
            print(x, "is not a Leap Year")
    else:
        print(x, "is a Leap Year")
else:
    print(x, "is not a Leap Year") """


#Using Ternary operator

""" x=2024

result=True if x%4==0 and x%100!=0 or x%400!=0 else False
print(result)
 """
# USing calender module

""" import calendar

year=2024
result=calendar.isleap(year)
print(result) """




leap=lambda year : year%4==0 and year%100!=0 or year%400!=0
result=leap(2024)
print(result)






