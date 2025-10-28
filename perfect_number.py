# sum=0
# def strong_Number(num):
#     global sum
#     for i in range(1,num):
#         if num%i==0:
#             sum=sum+i
#         else:
#             pass
    

#     return sum
# result=strong_Number(28)
# print(result)
sum=0
def strong_Number(num,i=1):
    global sum
    if i<=(num/2):
        if num%i==0:
            sum=sum+i

        strong_Number(num,i+1)
    return sum

    
        

result=strong_Number(28)
print(result)       
        
        
    
    
        

