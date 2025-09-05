""" import math
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

 """


import math
primes=[2,3]
min=2
max=10

for i in range(min,max+1):
    flag=0
    if i%2==0:
        continue
    if i%3==0:
        continue
    iter=3
    while iter<round(math.sqrt(max)):
        if i%iter==0:
            flag=1
            break
        iter+=2

    if flag==0:
       primes.append(i)


print(primes)

