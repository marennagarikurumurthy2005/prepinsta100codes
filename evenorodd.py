x=int(input("Enter a Number:"))
if x%2==0:
    print(x,"is even")
else:
    print(x,"is odd")




# Using Ternary Operator



y=int(input("Enter a Number:"))

result="even" if y%2==0 else "odd"
print(result)
print(type(result)) 



# Using bitwise Operator

z=int(input("Enter the Number:"))
if z&1:
    print("odd")
else:
    print("even")
