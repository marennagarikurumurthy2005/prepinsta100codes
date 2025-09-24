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
data2="anyname"
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



#Check any number is prime number or not

""" num=13
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
    else:
        flag=0
if flag==0:
    print(num,"is prime")
else:
    print(num,"Not prime") """

#Print vowels in a string and count them
 # type 1
""" vowels=['a','e','i','o','u','A','E','I','O','U']
word="ammabangarthalli"
total_vowels=[]
vowels_count=0
for i in word:
    if i in vowels:
        total_vowels.append(i)
        vowels_count+=1
print(total_vowels,vowels_count) """

 # type 2

""" vowels=['a','e','i','o','u','A','E','I','O','U']
word="ammabangarthalli"
total_vowels=[]
vowels_count=0
for i in word:
    if i in vowels:
            if i not in total_vowels:
                total_vowels.append(i)
                vowels_count+=1
print(total_vowels,vowels_count) """



# Type 3 

""" vowels=['a','e','i','o','u','A','E','I','O','U']
word="ammabangarthalli"
total_vowels=[]
vowels_count=0
for i in word:
    if i in vowels:
            if i not in total_vowels:
                total_vowels.append(i)
            vowels_count+=1
print(total_vowels,vowels_count) """


# Palindrome on name
     # method 1

     
""" data5="madam"
rev_data5=data5[::-1]
if data5==rev_data5:
    print(data5,"is a palindrome")
else:
    print(data5,"not a palindrome") """


            # method 2

""" data=''

for i in range(1,len(data5)+1):
    data=data+(data5[-i])
print(data) """


#Find wide spaces between string And Remove spaces between string
   #method 1
""" word="Im Kurumurthy Marennagari and i like her"
for ch in word:
    if ch!=" ":
        print(ch,end="") """

    # method 2

""" count=0
index_place=[]
word="Im     Kurumurthy        Marennagari       and i    like her"
for i in range(len(word)-1):
    if word[i]==" " and word[i+1]==" ":
        count+=1
        index_place.append(i)
        pass
    else:
        print(word[i],end='')

print("\n" ,count)
print(index_place) """

# Factorial of a given number
    #method 1
""" def is_factorial(num):
    if num==0:
        return 1
    else:
        return num*is_factorial(num-1)
result=is_factorial(5)
print(result) """
 

   #method2

""" num=5
if num==0:
    print("factorial of 0 is 1")
else:
    result=1
    for i in range(1,num+1):
        result=result*i
print(result) """


# Converting list into string Ex python

""" data3=['p','y','t']
result=""
for i in data3:
    result=result+i
print(result)
print(type(result)) """

#  Compare 3 numbers without using logical operators.


 # method 1

num1=100
num2=222
num3=30



if num1<num2:
    if num1<num3:
        print(num1,"num1 is smaller")
    else:
        print(num3,"num3 is smallar")
else:
    if num2<num3:
        print(num2,"num2 is smaller")
    else:
        print(num3," num3 is smallar")



        
