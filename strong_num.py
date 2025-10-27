def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

num=int(input("Enter number: "))
temp=num
sum=0
while num>0:
    last=num%10
    sum=sum+fact(last)
    num=num//10

if temp==sum:
    print("strong num")

else:
    print("Not a strong num")


