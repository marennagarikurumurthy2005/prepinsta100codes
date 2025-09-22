minimum=1
maximum=100000
arm_list=[]
for i in range(minimum,maximum):
    temp=i
    num=i
    sum=0
    n=len(str(i))
    while num>0:
        reminder=num%10
        sum=sum+(reminder**n)
        num=num//10

    if temp==sum:
        arm_list.append(sum)
print(arm_list)
    