import math
min=2
max=25
list=[]

for i in range(min,max+1):
    flag=0
    for j in range(2,round(math.sqrt(i))):
        if i%j==0:
            flag=1
            break
        else:
            flag=0

        
    if flag==0:
        list.append(i)


print(list)