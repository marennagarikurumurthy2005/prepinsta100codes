import math
# using O(n)
""" num=100
for i in range(1,num):
    if i!=1 and num%i==0:
        print(i) """

# using O(sqrt(n)) 
""" num=100
for i in range(1,int(math.sqrt(num))):
    divisor=0
    if i!=1 and num%i==0:
        divisor=int(num/i)
        print(f"{i}\n{divisor}") """
        


