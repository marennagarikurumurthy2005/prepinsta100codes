""" num="12345"
sum=0
for i in num:
    sum=sum+int(i)
   
print(sum)  




 """


""" 
num=1258
sum=0
for i in range(0,len(str(num))):
    ex=num%10
    num=int(num/10)
    sum=sum+ex
print(sum) """



""" 
def digit_sum(num):
    
    if len(num)==0:
        return 0
    else:
        return int(num[0])+digit_sum(num[1:])
    

num="125"
        
result=digit_sum(num)
print(result) """


""" 
num=int(input("Enter Num:"))

def find_Sum(num):
    if num==0:
        return 0
    return num%10 + find_Sum(int(num/10))
result=find_Sum(num)
print(result)


 """




""" 
def add_sum(num):
    return sum(ord(ch)-ord('0') for ch in num)




num="12345"
result=add_sum(num)
print(result)
 """




