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


""" for l in range(2,round((x/2))+1):

    if x%l==0:
        flag=1
        break
   
if flag==1:
    print("Not Prime")
else:
    print("Prime") """




""" if x<=3:
    flag=0

else:
    for m in range(2,int(math.sqrt(x))+1):
        if  x%m==0:
            flag=1
            break


if flag==1:
    print("Not Prime")
else:
    print("Prime")    
 """



""" if x<=3:
    flag=0
else:
    if x%2==0:
        flag=1
    else:
        for n in range(2,int(math.sqrt(x))+1,2):
            if  x%n==0:
                flag=1
                break
        

if flag==1:
    print("Not Prime")
else:
    print("Prime")   """  


iter=2

def is_recusion(num,iter):
    if num==iter:
        return True
    if num%iter==0:
        return False
    if num<iter:
        return False
    is_recusion(num,iter+1)
if is_recusion(x,iter)==True:
    print("Prime")
else:
    print("Not prime")    

