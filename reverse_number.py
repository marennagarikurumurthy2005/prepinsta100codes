""" # reverse as a list 

num=123
rev=[]
for i in range(0,len(str(num))):
    new_num=num%10
    num=int(num/10)
    rev.append(new_num)
print(rev) """



""" 
#reverse as a number 
num=1568
rev=0
while num>0:
    reminder=num%10
    rev=(rev*10)+reminder
    num=num//10
print(rev)


 """
""" 
#using String slicing

string="12345"
rev=string[::-1]
print(rev)

 """



def reverse(num,rev):
 
    if num==0:
        return rev
    else:
        reminder=int(num%10)
        rev=(rev*10)+reminder
        return reverse(int(num/10),rev)
result=reverse(1234,0)
print(result)