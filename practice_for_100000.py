#Return data types of a data

""" x=10
print(type(x)) """


# Converting an integer into decimal
""" y=float(x)
print(y) """

#Reverse a string

""" data1="Murthy"
rev_data1=data1[::-1]
print(rev_data1) """

#Counting vowels in give word

""" vowels=['a','e','i','o','u','A','E','I','O','U']
data2="revathi"
count=0
for i in data2:
    if i in vowels:
        count+=1
    
print(count) """

# Finding Maximum number in a list
# method 1 using inbuilt function


""" data3=[4,5,3,2,89,7,46]
print(max(data3)) """

# without using inbuilt functions

""" data3=[4,5,3,2,89,7,46,701,985]
for i in data3:
    for j in data3:
        if i<=j:
            i=j
print(i) """


#Adding 2 list elements
# merging 2 list
""" data1=[1,2,3]
data2=[4,5,6]
data3=data1+data2
print(data3) """

# adding elements of list

""" data4=[]
for i in range(len(data2)):
    x=data1[i]+data2[i]
    data4.append(x)
print(data4) """


# Reverse a number

""" num=123
num_string=str(num)
print(num)

#method 1
rev_num_string=num_string[::-1]
print(rev_num_string)
print(type(rev_num_string))

# method 2
rev_num=0
for i in range(len(str(num))):
    reminder=num%10
    rev_num=(rev_num*10)+reminder
    num=num//10
print(rev_num)
print(type(rev_num)) """


#Print 1 to 20 even number and odd numbers

""" even=[]
odd=[]
for i in range(1,20):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even",even,"Odd",odd) """








   



