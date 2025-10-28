def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

# num=int(input("Enter number: "))
# temp=num
# sum=0
# while num>0:
#     last=num%10
#     sum=sum+fact(last)
#     num=num//10

# if temp==sum:
#     print("strong num")

# else:
#     print("Not a strong num")
sum=0
def check_Strong(num):
    global sum
    if num==0:
        return sum
    else:
        last=num%10
        sum=sum+fact(last)
        return check_Strong(num//10)


num=int(input("Enter number :"))
result=check_Strong(num)
if result==num:
    print("Strong num")
else:
    print("Not a strong num")



