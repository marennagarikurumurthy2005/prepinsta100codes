""" num=112211
temp=str(num)
rev=temp[::-1]
rev=int(rev)

if num==rev:
    print("Palindrome")
else:
    print("Not Palindrome") """


""" 
num=1221
number=num
rev=0
while num>0:
    reminder=num%10
    rev=(rev*10)+reminder
    num=num//10

print(rev)
if number==rev:
    print("Palindrome")
else:
    print("Not Palindrome") """


""" def is_palindrome(num,rev):
    if num==0:
        return rev

    else:
        reminder=num%10
        rev=(rev*10)+reminder
        return is_palindrome(int(num/10),rev)
    
num=112211
result=is_palindrome(num,0)
if num==result:
    print(num,"is Palindrome")
else:
    print(num,"is not a Palindrome")

 """



""" def palindrome(num):
    for i in range(0,len(num)):
        if num[i]!=num[len(num)-1-i]:
            return False
       
    return True
    
num="12367321"
print("Palindrome") if palindrome(num) else print("Not palindrome")
     """


""" 

def palindrome(num):
    rev=''.join(reversed(num))
    if num==rev:
        return True
    else:
        False



num="1278921"
print("Palindrome") if palindrome(num) else print("not")

 """
""" 
string="12321"
rev=""
for char in string:
    rev=char+rev
if rev==string:
    print("Palindrome")
else:
    print("Not a palindrome")
 """


""" string="1234"
flag=0
j=-1
for char in string:
    if char!=string[j]:
        flag=1
        break
    j=j-1
print("palindrome") if flag==0 else print("not") """



