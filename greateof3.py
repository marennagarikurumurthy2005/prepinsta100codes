num1,num2,num3=10,20,30
if num1>num2 and num1>num3:
    print("NUM1")
elif num2>num1 and num2>num3:
    print("NUM2")
else:
    print("NUM3")




# Using nested if


if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
    else :
        print(num3)



#USing ternary operator

num1, num2, num3 = 10 , 30 , 20
max = num1 if num1>num2 else num2
max = num3 if num3>max else max
print(max)