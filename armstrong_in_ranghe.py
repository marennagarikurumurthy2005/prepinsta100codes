minimum=1
maximum=1800
arm_list=[]
for i in range(minimum,maximum):
    temp=i
    sum=0
    for j in range(len(str(i))):
        reminder=i%10
        sum=sum+(reminder**3)
        i=i//10

    if temp==sum:
        arm_list.append(sum)
print(arm_list)
    