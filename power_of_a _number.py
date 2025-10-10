""" # using simple iteration
num=10
power=3
total=1
if num==0:
    print(total)
else:
    for i in range(0,power):
        total=total*num

    print(total) """

# using power function

""" import math
print(math.pow(3,3)) """



#Using python operator
""" num=2
power=3
print(num**power) """

# using recursion

def power(num,power):
    if power==0:
        return 1
    else:
        return num*power(num,pow-1)
    
print(pow(5,2))




