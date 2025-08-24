sum=0
n=5
for i in range(2,n+1):
    sum=sum+i
print(sum)




#Using Formula

a=2
b=5
sum=b*(b+1)/2-a*(a+1)/2+a
print(sum)



# Using recurssion



def sum(total,min,max):

    
    if min>max:
        return total
    else:
        return max+sum(total,min,max-1)
x=sum(0,1,10)
print(x)
        
        
        
