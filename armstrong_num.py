num=int(input("Enter a Number:"))
temp=num
total_sum=0
power=len(str(num))
print(power)
while num>0:
    reminder=0

    reminder=num%10
    total_sum=total_sum+reminder**power
    num=num//10

    

print(total_sum)

if temp==total_sum:
    print("It is a armstrong number")
else:
    print("Not")

