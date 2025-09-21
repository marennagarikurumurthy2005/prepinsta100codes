""" num=int(input("Enter a Number:"))
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





 """






def is_Armstrong(num,sum=0):
    
    if num==0:
        return sum
    else:
        reminder=num%10
        sum=sum+reminder**num_length
        
        return is_Armstrong(int(num/10),sum)
    
    

num=int(input("Enter number:")) 
num_length=len(str(num)) 
result=is_Armstrong(num,0)
if num==result:
    print(num,"is a armstrong number")
else:
    print(num,"is not armstrong")
    print("try again")
    


