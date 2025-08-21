#using for loop
n=int(input("Enter N:"))
result=0
for i in range(0,n+1):
    result=result+i

print(result)



#Using formula


m=int(input("Enter M:"))

result =m*(m+1)/2
print(result) 


#Using Recurrsion
num=int(input("Enter Number:"))

def recurssion(num):
    if num>=0:
        if num==1:
            return 1
        else:
            return num+recurssion(num-1)
    else:
        return "Num is Negative"
    

result=recurssion(num)
print(result)



