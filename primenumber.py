import math
x=int(input("Enter Number:"))
""" list=[]

for i in range(2,x+1):
    if x%i==0:
        list.append(i)
retult=True if len(list)==1 else False
print(retult) """



""" 
flag=0  
        
for j in range(2,x):
    if x%j==0:
        flag=1
        break
if flag==1:
    print("Not prime")
else:
    print("Prime")
 """

flag=0

for l in range(2,round(math.sqrt(x))):

    if l>6 and x%l==0:
        flag=1
        break
if flag==1:
    print("Not Prime")
else:
    print("Prime")
    

       